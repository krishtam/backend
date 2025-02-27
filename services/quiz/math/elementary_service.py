from mathgenerator import mathgen
from models import MathProblem

class ElementaryService:
    """
    Service for generating elementary school-level math problems.
    """

    # 🏷️ Addition & Subtraction
    def generate_addition_problem(self) -> MathProblem:
        """Generate an addition problem."""
        problem, solution = mathgen.addition()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="Elementary",
            unit_id=None,  # You might want to set these properly
            topic_id=None  # You might want to set these properly
        )

    def generate_subtraction_problem(self) -> MathProblem:
        """Generate a subtraction problem."""
        problem, solution = mathgen.subtraction()
        return MathProblem(
            problem=problem,
            solution=str(solution),
            grade_level="Elementary",
            unit_id=None,
            topic_id=None
        )

    def generate_absolute_difference_problem(self) -> MathProblem:
        """Generate an absolute difference problem."""
        problem, solution = mathgen.absolute_difference()
        return MathProblem(
            grade_level="Elementary",
            unit="Addition & Subtraction",
            topic="Absolute Difference",
            problem=problem,
            solution=str(solution)
        )

    # 🏷️ Multiplication & Division
    def generate_multiplication_problem(self) -> MathProblem:
        """Generate a multiplication problem."""
        problem, solution = mathgen.multiplication()
        return MathProblem(
            grade_level="Elementary",
            unit="Multiplication & Division",
            topic="Multiplication",
            problem=problem,
            solution=str(solution)
        )

    def generate_division_problem(self) -> MathProblem:
        """Generate a division problem."""
        problem, solution = mathgen.division()
        return MathProblem(
            grade_level="Elementary",
            unit="Multiplication & Division",
            topic="Division",
            problem=problem,
            solution=str(solution)
        )

    # 🏷️ Place Value & Number Sense
    def generate_fraction_to_decimal_problem(self) -> MathProblem:
        """Generate a fraction-to-decimal conversion problem."""
        problem, solution = mathgen.fraction_to_decimal()
        return MathProblem(
            grade_level="Elementary",
            unit="Place Value & Number Sense",
            topic="Fraction to Decimal",
            problem=problem,
            solution=str(solution)
        )

    def generate_square_problem(self) -> MathProblem:
        """Generate a square problem."""
        problem, solution = mathgen.square()
        return MathProblem(
            grade_level="Elementary",
            unit="Place Value & Number Sense",
            topic="Square",
            problem=problem,
            solution=str(solution)
        )

    def generate_square_root_problem(self) -> MathProblem:
        """Generate a square root problem."""
        problem, solution = mathgen.square_root()
        return MathProblem(
            grade_level="Elementary",
            unit="Place Value & Number Sense",
            topic="Square Root",
            problem=problem,
            solution=str(solution)
        )

    def generate_cube_root_problem(self) -> MathProblem:
        """Generate a cube root problem."""
        problem, solution = mathgen.cube_root()
        return MathProblem(
            grade_level="Elementary",
            unit="Place Value & Number Sense",
            topic="Cube Root",
            problem=problem,
            solution=str(solution)
        )

    def generate_factorial_problem(self) -> MathProblem:
        """Generate a factorial problem."""
        problem, solution = mathgen.factorial()
        return MathProblem(
            grade_level="Elementary",
            unit="Place Value & Number Sense",
            topic="Factorial",
            problem=problem,
            solution=str(solution)
        )

    def generate_gcd_problem(self) -> MathProblem:
        """Generate a greatest common divisor (GCD) problem."""
        problem, solution = mathgen.greatest_common_divisor()
        return MathProblem(
            grade_level="Elementary",
            unit="Place Value & Number Sense",
            topic="Greatest Common Divisor",
            problem=problem,
            solution=str(solution)
        )

    def generate_is_prime_problem(self) -> MathProblem:
        """Generate a prime number check problem."""
        problem, solution = mathgen.is_prime()
        return MathProblem(
            grade_level="Elementary",
            unit="Place Value & Number Sense",
            topic="Prime Number Check",
            problem=problem,
            solution=str(solution)
        )

    def generate_is_composite_problem(self) -> MathProblem:
        """Generate a composite number check problem."""
        problem, solution = mathgen.is_composite()
        return MathProblem(
            grade_level="Elementary",
            unit="Place Value & Number Sense",
            topic="Composite Number Check",
            problem=problem,
            solution=str(solution)
        )

    # 🏷️ Fractions & Decimals
    def generate_compare_fractions_problem(self) -> MathProblem:
        """Generate a fraction comparison problem."""
        problem, solution = mathgen.compare_fractions()
        return MathProblem(
            grade_level="Elementary",
            unit="Fractions & Decimals",
            topic="Compare Fractions",
            problem=problem,
            solution=str(solution)
        )

    def generate_fraction_multiplication_problem(self) -> MathProblem:
        """Generate a fraction multiplication problem."""
        problem, solution = mathgen.fraction_multiplication()
        return MathProblem(
            grade_level="Elementary",
            unit="Fractions & Decimals",
            topic="Fraction Multiplication",
            problem=problem,
            solution=str(solution)
        )

    def generate_divide_fractions_problem(self) -> MathProblem:
        """Generate a fraction division problem."""
        problem, solution = mathgen.divide_fractions()
        return MathProblem(
            grade_level="Elementary",
            unit="Fractions & Decimals",
            topic="Divide Fractions",
            problem=problem,
            solution=str(solution)
        )

    def generate_simplify_square_root_problem(self) -> MathProblem:
        """Generate a square root simplification problem."""
        problem, solution = mathgen.simplify_square_root()
        return MathProblem(
            grade_level="Elementary",
            unit="Fractions & Decimals",
            topic="Simplify Square Root",
            problem=problem,
            solution=str(solution)
        )