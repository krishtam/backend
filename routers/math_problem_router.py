from fastapi import APIRouter, Depends, HTTPException
from models.topic import Topic
from models.db import get_db
from models.unit import Unit
from services.math_service import GeneralMathService
from services.quiz.math.elementary_service import ElementaryService
from services.quiz.math.midde_service import MiddleSchoolService
from services.quiz.math.hs_service import HighSchoolService
from services.quiz.math.advanced_hs_service import AdvancedHighSchoolService
from models import MathProblem
from schemas.mathProblem import MathProblemBase  # Pydantic schema for MathProblem
from typing import List
from sqlalchemy.orm import Session
import logging
from services.topic_service import TopicService

router = APIRouter()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@router.get("/units-with-topics")
def get_all_units_with_topics(db: Session = Depends(get_db)):
    """
    Retrieve all units with their associated topics.
    """
    try:
        units = db.query(Unit).all()

        response = []
        for unit in units:
            unit_data = {
                "unit_id": unit.id,
                "unit_name": unit.name,
                "topics": [{"topic_id": topic.id, "topic_name": topic.name} for topic in unit.topics]
            }
            response.append(unit_data)

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all units
@router.get("/units")
def get_all_units(db: Session = Depends(get_db)):
    """
    Retrieve all units.
    """
    try:
        units = db.query(Unit).all()

        if not units:
            raise HTTPException(status_code=404, detail="No units found")

        return [{"unit_id": unit.id, "unit_name": unit.name} for unit in units]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all topics within a specific unit
@router.get("/unit/{unit_id}")
def get_topics_by_unit(unit_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all topics within a specific unit.
    """
    try:
        logger.debug(f"Fetching unit with ID: {unit_id}")

        # Find the unit
        unit = db.query(Unit).filter(Unit.id == unit_id).first()

        if not unit:
            logger.error(f"Unit with ID {unit_id} not found")
            raise HTTPException(status_code=404, detail="Unit not found")

        logger.debug(f"Unit found: {unit.name}")

        # Get all topics related to this unit
        topics = unit.topics

        if not topics:
            logger.warning(f"No topics found for unit with ID {unit_id}")
            raise HTTPException(status_code=404, detail="No topics found for this unit")

        logger.debug(f"Topics found: {[topic.name for topic in topics]}")

        return [{"topic_id": topic.id, "topic_name": topic.name} for topic in topics]

    except Exception as e:
        logger.error(f"Error fetching topics for unit {unit_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Get all units for a specific level (subject or grade level)
@router.get("/level/{level_id}")
def get_units_by_level(level_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all units for a specific level.
    """
    try:
        # Filter units by level (like grade level or subject level)
        units = db.query(Unit).filter(Unit.level_id == level_id).all()

        if not units:
            raise HTTPException(status_code=404, detail="No units found for this level")

        return [{"unit_id": unit.id, "unit_name": unit.name} for unit in units]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/general/{level}/{topic}", response_model=MathProblemBase)
def get_dynamic_math_problem(level: str, topic: str, 
                             elementary_service: ElementaryService = Depends(),
                             middle_school_service: MiddleSchoolService = Depends(),
                             high_school_service: HighSchoolService = Depends(),
                             advanced_hs_service: AdvancedHighSchoolService = Depends()):
    """
    General route to retrieve a dynamically generated math problem based on level and topic.
    """

    # Map levels to their corresponding services
    services = {
        'elementary': elementary_service,
        'middle_school': middle_school_service,
        'high_school': high_school_service,
        'advanced_high_school': advanced_hs_service
    }

    # Validate level
    if level not in services:
        raise HTTPException(status_code=404, detail="Level not found")

    # Initialize TopicService
    topic_service = TopicService()

    # Convert topic to function name
    function_name = topic_service.get_function_details(topic)

    # Get the service for the given level
    service = services[level]

    # Validate if function exists in the service
    if not hasattr(service, function_name):
        raise HTTPException(status_code=404, detail="Function not found in the selected level")

    # Call the function dynamically
    function = getattr(service, function_name)
    result = function()  # Expected to return an instance of MathProblem (ORM model)

    # Convert ORM object to Pydantic model
    if isinstance(result, dict):  
        return MathProblemBase(**result)  # If already a dict, convert directly
    elif hasattr(result, "__dict__"):  
        return MathProblemBase(**result.__dict__)  # Convert ORM model to dict
    else:
        raise HTTPException(status_code=500, detail="Invalid math problem format")

@router.get("/topic/{topic_name}/level")
def get_topic_level(topic_name: str):
    """
    Get the level (elementary, middle_school, high_school, advanced_high_school) for a given topic.
    """
    topic_service = TopicService()
    return {"topic": topic_name, "level": topic_service.get_topic_level(topic_name)}


@router.get("/topics-by-level")
def get_topics_by_level():
    """
    Get all topics organized by their levels.
    """
    topic_service = TopicService()
    topics_by_level = {
        "elementary": [],
        "middle_school": [],
        "high_school": [],
        "advanced_high_school": []
    }
    
    for topic in topic_service.topic_to_level.keys():
        level = topic_service.topic_to_level[topic]
        topics_by_level[level].append(topic)
    
    return topics_by_level