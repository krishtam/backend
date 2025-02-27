from mathgenerator import mathgen
from models import MathProblem

class HighSchoolService:
    """
    Service for generating high school-level math problems (Algebra 1, Geometry, Statistics).
    """

    # 🏷️ Algebra 1 & Linear Equations
    # Linear Functions
    def generate_intersection_of_two_lines(self) -> MathProblem:
        """Generate intersection of two lines problem."""
        problem, solution = mathgen.intersection_of_two_lines()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_line_equation_from_2_points(self) -> MathProblem:
        """Generate line equation from two points problem."""
        problem, solution = mathgen.line_equation_from_2_points()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    # Quadratics & Polynomials
    def generate_quadratic_equation(self) -> MathProblem:
        """Generate quadratic equation problem."""
        problem, solution = mathgen.quadratic_equation()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_complex_quadratic(self) -> MathProblem:
        """Generate complex quadratic problem."""
        problem, solution = mathgen.complex_quadratic()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    # Logarithms & Exponents
    def generate_logarithm_problem(self) -> MathProblem:
        """Generate logarithm problem."""
        problem, solution = mathgen.log()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )


    # 🏷️ Geometry & Trigonometry
    # Triangle Properties & Theorems
    def generate_pythagorean_theorem(self) -> MathProblem:
        """Generate Pythagorean Theorem problem."""
        problem, solution = mathgen.pythagorean_theorem()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_basic_trigonometry(self) -> MathProblem:
        """Generate basic trigonometry problem."""
        problem, solution = mathgen.basic_trigonometry()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    # Advanced Volume & Surface Area
    def generate_surface_area_pyramid(self) -> MathProblem:
        """Generate surface area of a pyramid problem."""
        problem, solution = mathgen.surface_area_pyramid()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_surface_area_cone(self) -> MathProblem:
        """Generate surface area of a cone problem."""
        problem, solution = mathgen.surface_area_cone()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_volume_pyramid(self) -> MathProblem:
        """Generate volume of a pyramid problem."""
        problem, solution = mathgen.volume_pyramid()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_volume_cone(self) -> MathProblem:
        """Generate volume of a cone problem."""
        problem, solution = mathgen.volume_cone()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_volume_cone_frustum(self) -> MathProblem:
        """Generate volume of a cone frustum problem."""
        problem, solution = mathgen.volume_cone_frustum()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_volume_hemisphere(self) -> MathProblem:
        """Generate volume of a hemisphere problem."""
        problem, solution = mathgen.volume_hemisphere()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )


    # 🏷️ Probability & Statistics
    # Data Analysis
    def generate_data_summary(self) -> MathProblem:
        """Generate data summary problem."""
        problem, solution = mathgen.data_summary()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_confidence_interval(self) -> MathProblem:
        """Generate confidence interval problem."""
        problem, solution = mathgen.confidence_interval()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    # Probability Models
    def generate_conditional_probability(self) -> MathProblem:
        """Generate conditional probability problem."""
        problem, solution = mathgen.conditional_probability()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_binomial_distribution(self) -> MathProblem:
        """Generate binomial distribution problem."""
        problem, solution = mathgen.binomial_distribution()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_system_of_equations_problem(self) -> MathProblem:
        problem, solution = mathgen.system_of_equations()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )

    def generate_distance_formula_problem(self) -> MathProblem:
        problem, solution = mathgen.distance_formula()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="High School",
            unit_id=None,
            topic_id=None
        )
