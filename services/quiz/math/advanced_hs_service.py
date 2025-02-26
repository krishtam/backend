from mathgenerator import mathgen
from models import MathProblem

class AdvancedHighSchoolService:
    """
    Service for generating advanced high school-level math problems (Algebra 2, Precalculus, Calculus).
    """

    # 🏷️ Algebra 2 & Advanced Functions
    # Matrices & Vectors
    def generate_int_matrix_22_determinant(self) -> MathProblem:
        """Generate determinant of a 2x2 matrix problem."""
        problem, solution = mathgen.int_matrix_22_determinant()
        return MathProblem(
            grade_level="High School",
            unit="Algebra 2 & Advanced Functions",
            topic="Determinant of 2x2 Matrix",
            problem=problem,
            solution=str(solution)
        )

    def generate_invert_matrix(self) -> MathProblem:
        """Generate matrix inversion problem."""
        problem, solution = mathgen.invert_matrix()
        return MathProblem(
            grade_level="High School",
            unit="Algebra 2 & Advanced Functions",
            topic="Matrix Inversion",
            problem=problem,
            solution=str(solution)
        )

    def generate_matrix_multiplication(self) -> MathProblem:
        """Generate matrix multiplication problem."""
        problem, solution = mathgen.matrix_multiplication()
        return MathProblem(
            grade_level="High School",
            unit="Algebra 2 & Advanced Functions",
            topic="Matrix Multiplication",
            problem=problem,
            solution=str(solution)
        )

    def generate_vector_cross(self) -> MathProblem:
        """Generate vector cross product problem."""
        problem, solution = mathgen.vector_cross()
        return MathProblem(
            grade_level="High School",
            unit="Algebra 2 & Advanced Functions",
            topic="Vector Cross Product",
            problem=problem,
            solution=str(solution)
        )

    def generate_vector_dot(self) -> MathProblem:
        """Generate vector dot product problem."""
        problem, solution = mathgen.vector_dot()
        return MathProblem(
            grade_level="High School",
            unit="Algebra 2 & Advanced Functions",
            topic="Vector Dot Product",
            problem=problem,
            solution=str(solution)
        )

    def generate_orthogonal_projection(self) -> MathProblem:
        """Generate orthogonal projection problem."""
        problem, solution = mathgen.orthogonal_projection()
        return MathProblem(
            grade_level="High School",
            unit="Algebra 2 & Advanced Functions",
            topic="Orthogonal Projection",
            problem=problem,
            solution=str(solution)
        )


    # 🏷️ Complex Numbers
    def generate_multiply_complex_numbers(self) -> MathProblem:
        """Generate complex number multiplication problem."""
        problem, solution = mathgen.multiply_complex_numbers()
        return MathProblem(
            grade_level="High School",
            unit="Complex Numbers",
            topic="Multiply Complex Numbers",
            problem=problem,
            solution=str(solution)
        )

    def generate_complex_to_polar(self) -> MathProblem:
        """Generate conversion from complex number to polar form."""
        problem, solution = mathgen.complex_to_polar()
        return MathProblem(
            grade_level="High School",
            unit="Complex Numbers",
            topic="Complex to Polar",
            problem=problem,
            solution=str(solution)
        )


    # 🏷️ Sequences & Series
    def generate_arithmetic_progression_sum(self) -> MathProblem:
        """Generate arithmetic progression sum problem."""
        problem, solution = mathgen.arithmetic_progression_sum()
        return MathProblem(
            grade_level="High School",
            unit="Sequences & Series",
            topic="Arithmetic Progression Sum",
            problem=problem,
            solution=str(solution)
        )

    def generate_arithmetic_progression_term(self) -> MathProblem:
        """Generate nth term of arithmetic progression problem."""
        problem, solution = mathgen.arithmetic_progression_term()
        return MathProblem(
            grade_level="High School",
            unit="Sequences & Series",
            topic="Arithmetic Progression Term",
            problem=problem,
            solution=str(solution)
        )

    def generate_geometric_progression(self) -> MathProblem:
        """Generate geometric progression problem."""
        problem, solution = mathgen.geometric_progression()
        return MathProblem(
            grade_level="High School",
            unit="Sequences & Series",
            topic="Geometric Progression",
            problem=problem,
            solution=str(solution)
        )

    def generate_geometric_mean(self) -> MathProblem:
        """Generate geometric mean problem."""
        problem, solution = mathgen.geometric_mean()
        return MathProblem(
            grade_level="High School",
            unit="Sequences & Series",
            topic="Geometric Mean",
            problem=problem,
            solution=str(solution)
        )

    def generate_harmonic_mean(self) -> MathProblem:
        """Generate harmonic mean problem."""
        problem, solution = mathgen.harmonic_mean()
        return MathProblem(
            grade_level="High School",
            unit="Sequences & Series",
            topic="Harmonic Mean",
            problem=problem,
            solution=str(solution)
        )


    # 🏷️ Trigonometry & Advanced Geometry
    def generate_angle_btw_vectors(self) -> MathProblem:
        """Generate angle between vectors problem."""
        problem, solution = mathgen.angle_btw_vectors()
        return MathProblem(
            grade_level="High School",
            unit="Trigonometry & Advanced Geometry",
            topic="Angle Between Vectors",
            problem=problem,
            solution=str(solution)
        )

    def generate_degree_to_rad(self) -> MathProblem:
        """Generate degree to radian conversion problem."""
        problem, solution = mathgen.degree_to_rad()
        return MathProblem(
            grade_level="High School",
            unit="Trigonometry & Advanced Geometry",
            topic="Degree to Radian Conversion",
            problem=problem,
            solution=str(solution)
        )

    def generate_radian_to_deg(self) -> MathProblem:
        """Generate radian to degree conversion problem."""
        problem, solution = mathgen.radian_to_deg()
        return MathProblem(
            grade_level="High School",
            unit="Trigonometry & Advanced Geometry",
            topic="Radian to Degree Conversion",
            problem=problem,
            solution=str(solution)
        )


    # 🏷️ Calculus
    # Derivatives
    def generate_power_rule_differentiation(self) -> MathProblem:
        """Generate power rule differentiation problem."""
        problem, solution = mathgen.power_rule_differentiation()
        return MathProblem(
            grade_level="High School",
            unit="Calculus",
            topic="Power Rule Differentiation",
            problem=problem,
            solution=str(solution)
        )

    def generate_trig_differentiation(self) -> MathProblem:
        """Generate trigonometric differentiation problem."""
        problem, solution = mathgen.trig_differentiation()
        return MathProblem(
            grade_level="High School",
            unit="Calculus",
            topic="Trigonometric Differentiation",
            problem=problem,
            solution=str(solution)
        )


    # Integrals
    def generate_power_rule_integration(self) -> MathProblem:
        """Generate power rule integration problem."""
        problem, solution = mathgen.power_rule_integration()
        return MathProblem(
            grade_level="High School",
            unit="Calculus",
            topic="Power Rule Integration",
            problem=problem,
            solution=str(solution)
        )

    def generate_definite_integral(self) -> MathProblem:
        """Generate definite integral problem."""
        problem, solution = mathgen.definite_integral()
        return MathProblem(
            grade_level="High School",
            unit="Calculus",
            topic="Definite Integral",
            problem=problem,
            solution=str(solution)
        )


    # Applications
    def generate_stationary_points(self) -> MathProblem:
        """Generate stationary points problem."""
        problem, solution = mathgen.stationary_points()
        return MathProblem(
            grade_level="High School",
            unit="Calculus",
            topic="Stationary Points",
            problem=problem,
            solution=str(solution)
        )
