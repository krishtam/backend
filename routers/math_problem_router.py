from fastapi import APIRouter, Depends, HTTPException
from models.topic import Topic
from models.db import get_db
from models.unit import Unit
from services.math_service import GeneralMathService
from services.quiz.math.elementary_service import ElementaryService
from services.quiz.math.midde_service import MiddleSchoolService
from services.quiz.math.hs_service import HighSchoolService
from services.quiz.math.advanced_hs_service import AdvancedHighSchoolService
from schemas.mathProblem import MathProblemResponse
from typing import List
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/topics-with-units")
def get_all_topics_with_units(db: Session = Depends(get_db)):
    """
    Retrieve all topics with their associated units.
    """
    try:
        topics = db.query(Topic).all()

        response = []
        for topic in topics:
            topic_data = {
                "topic_id": topic.id,
                "topic_name": topic.name,
                "units": [{"unit_id": unit.id, "unit_name": unit.name} for unit in topic.units]
            }
            response.append(topic_data)

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all topics for a specific level (subject or grade level)
@router.get("/level/{level_id}")
def get_topics_by_level(level_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all topics for a specific level.
    """
    try:
        # You might need to filter by level (like grade level or subject level)
        topics = db.query(Topic).filter(Topic.subject_id == level_id).all()

        if not topics:
            raise HTTPException(status_code=404, detail="No topics found for this level")

        return [{"topic_id": topic.id, "topic_name": topic.name} for topic in topics]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all topics within a specific unit
@router.get("/unit/{unit_id}")
def get_topics_by_unit(unit_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all topics within a specific unit.
    """
    try:
        # Find the unit
        unit = db.query(Unit).filter(Unit.id == unit_id).first()

        if not unit:
            raise HTTPException(status_code=404, detail="Unit not found")

        # Get all topics related to this unit
        topics = unit.topics

        if not topics:
            raise HTTPException(status_code=404, detail="No topics found for this unit")

        return [{"topic_id": topic.id, "topic_name": topic.name} for topic in topics]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create a general function that can handle any level/topic/function call dynamically
@router.get("/general/{level}/{topic}/{function_name}", response_model=MathProblemResponse)
def get_dynamic_math_problem(level: str, topic: str, function_name: str, 
                             general_service: GeneralMathService = Depends(),
                             elementary_service: ElementaryService = Depends(),
                             middle_school_service: MiddleSchoolService = Depends(),
                             high_school_service: HighSchoolService = Depends(),
                             advanced_hs_service: AdvancedHighSchoolService = Depends()):
    """
    General route to retrieve a dynamically generated math problem based on level, topic, and function.
    This dynamically accesses the correct function based on the `function_name`.
    """
    # Map levels to their corresponding services
    services = {
        'elementary': elementary_service,
        'middle_school': middle_school_service,
        'high_school': high_school_service,
        'advanced_high_school': advanced_hs_service
    }

    # Check if the level is valid
    if level not in services:
        raise HTTPException(status_code=404, detail="Level not found")

    # Get the appropriate service based on the level
    service = services[level]

    # Check if the function exists in the service
    if not hasattr(service, function_name):
        raise HTTPException(status_code=404, detail="Function not found")

    # Get the function dynamically from the service
    function = getattr(service, function_name)

    # Call the function and return the result
    return function()

# The services can have their methods dynamically accessed like this:
# for example, the elementary_service could have:
# def generate_addition_problem(self): ... (you would dynamically call it like this)

