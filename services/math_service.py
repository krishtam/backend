from services.quiz.math.elementary_service import ElementaryService  
from services.quiz.math.midde_service import MiddleSchoolService
from services.quiz.math.hs_service import HighSchoolService  
from services.quiz.math.advanced_hs_service import AdvancedHighSchoolService
#from quiz.math.puzzles.graph_puzzles_service import GraphPuzzlesService
#from quiz.math.puzzles.number_line_puzzles import NumberLinePuzzlesService

class GeneralMathService:
    """Handles generating math problems across all grade levels and categories."""

    @staticmethod
    def generate_problem(grade_level: str, category: str, topic: str):
        services = {
            "Elementary": ElementaryService,
            "Middle School": MiddleSchoolService,
            "High School": HighSchoolService,
            "Advanced High School": AdvancedHighSchoolService
            #"Graph Puzzles": GraphPuzzlesService,
            #"Shape Puzzles": ShapePuzzlesService,
            #"Number Line Puzzles": NumberLinePuzzlesService
        }

        if grade_level not in services:
            raise ValueError("Invalid grade level")
        
        service = services[grade_level]()
        
        function_name = f"generate_{topic.lower().replace(' ', '_')}_problem"
        if hasattr(service, function_name):
            return getattr(service, function_name)()
        else:
            raise ValueError("Invalid topic or function not implemented.")
