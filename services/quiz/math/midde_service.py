from mathgenerator import mathgen
from models import MathProblem

class MiddleSchoolService:
    """
    Service for generating middle school-level math problems.
    """

    # 🏷️ Expressions & Equations
    def generate_basic_algebra_problem(self) -> MathProblem:
        problem, solution = mathgen.basic_algebra()
        return MathProblem("Middle School", "Expressions & Equations", "Basic Algebra", problem, str(solution)
        )

    def generate_combine_like_terms_problem(self) -> MathProblem:
        problem, solution = mathgen.combine_like_terms()
        return MathProblem("Middle School", "Expressions & Equations", "Combine Like Terms", problem, str(solution))

    def generate_expanding_problem(self) -> MathProblem:
        problem, solution = mathgen.expanding()
        return MathProblem("Middle School", "Expressions & Equations", "Expanding", problem, str(solution))

    def generate_factoring_problem(self) -> MathProblem:
        problem, solution = mathgen.factoring()
        return MathProblem("Middle School", "Expressions & Equations", "Factoring", problem, str(solution))

    def generate_linear_equations_problem(self) -> MathProblem:
        problem, solution = mathgen.linear_equations()
        return MathProblem("Middle School", "Expressions & Equations", "Linear Equations", problem, str(solution))

    # 🏷️ Ratios, Proportions & Percents
    def generate_simple_interest_problem(self) -> MathProblem:
        problem, solution = mathgen.simple_interest()
        return MathProblem("Middle School", "Ratios, Proportions & Percents", "Simple Interest", problem, str(solution))

    def generate_compound_interest_problem(self) -> MathProblem:
        problem, solution = mathgen.compound_interest()
        return MathProblem("Middle School", "Ratios, Proportions & Percents", "Compound Interest", problem, str(solution))

    # 🏷️ Coordinate Plane & Graphing
    def generate_distance_two_points_problem(self) -> MathProblem:
        problem, solution = mathgen.distance_two_points()
        return MathProblem("Middle School", "Coordinate Plane & Graphing", "Distance Between Two Points", problem, str(solution))

    def generate_midpoint_of_two_points_problem(self) -> MathProblem:
        problem, solution = mathgen.midpoint_of_two_points()
        return MathProblem("Middle School", "Coordinate Plane & Graphing", "Midpoint of Two Points", problem, str(solution))

    def generate_line_equation_from_2_points_problem(self) -> MathProblem:
        problem, solution = mathgen.line_equation_from_2_points()
        return MathProblem("Middle School", "Coordinate Plane & Graphing", "Line Equation from Two Points", problem, str(solution))

    # 🏷️ Integers & Exponents
    def generate_exponentiation_problem(self) -> MathProblem:
        problem, solution = mathgen.exponentiation()
        return MathProblem("Middle School", "Integers & Exponents", "Exponentiation", problem, str(solution))

    def generate_power_of_powers_problem(self) -> MathProblem:
        problem, solution = mathgen.power_of_powers()
        return MathProblem("Middle School", "Integers & Exponents", "Power of Powers", problem, str(solution))

    def generate_quotient_of_power_same_base_problem(self) -> MathProblem:
        problem, solution = mathgen.quotient_of_power_same_base()
        return MathProblem("Middle School", "Integers & Exponents", "Quotient of Power (Same Base)", problem, str(solution))

    def generate_quotient_of_power_same_power_problem(self) -> MathProblem:
        problem, solution = mathgen.quotient_of_power_same_power()
        return MathProblem("Middle School", "Integers & Exponents", "Quotient of Power (Same Power)", problem, str(solution))

    # 🏷️ Geometry & Measurement

    # Angles & Shapes
    def generate_angle_regular_polygon_problem(self) -> MathProblem:
        problem, solution = mathgen.angle_regular_polygon()
        return MathProblem("Middle School", "Geometry & Measurement", "Angle of a Regular Polygon", problem, str(solution))

    def generate_third_angle_of_triangle_problem(self) -> MathProblem:
        problem, solution = mathgen.third_angle_of_triangle()
        return MathProblem("Middle School", "Geometry & Measurement", "Third Angle of a Triangle", problem, str(solution))

    def generate_fourth_angle_of_quadrilateral_problem(self) -> MathProblem:
        problem, solution = mathgen.fourth_angle_of_quadrilateral()
        return MathProblem("Middle School", "Geometry & Measurement", "Fourth Angle of a Quadrilateral", problem, str(solution))

    def generate_sum_of_polygon_angles_problem(self) -> MathProblem:
        problem, solution = mathgen.sum_of_polygon_angles()
        return MathProblem("Middle School", "Geometry & Measurement", "Sum of Polygon Angles", problem, str(solution))

    def generate_valid_triangle_problem(self) -> MathProblem:
        problem, solution = mathgen.valid_triangle()
        return MathProblem("Middle School", "Geometry & Measurement", "Valid Triangle Check", problem, str(solution))

    # Surface Area & Volume
    def generate_surface_area_cube_problem(self) -> MathProblem:
        problem, solution = mathgen.surface_area_cube()
        return MathProblem("Middle School", "Geometry & Measurement", "Surface Area of a Cube", problem, str(solution))

    def generate_surface_area_cylinder_problem(self) -> MathProblem:
        problem, solution = mathgen.surface_area_cylinder()
        return MathProblem("Middle School", "Geometry & Measurement", "Surface Area of a Cylinder", problem, str(solution))

    def generate_surface_area_sphere_problem(self) -> MathProblem:
        problem, solution = mathgen.surface_area_sphere()
        return MathProblem("Middle School", "Geometry & Measurement", "Surface Area of a Sphere", problem, str(solution))

    def generate_volume_cube_problem(self) -> MathProblem:
        problem, solution = mathgen.volume_cube()
        return MathProblem("Middle School", "Geometry & Measurement", "Volume of a Cube", problem, str(solution))

    def generate_volume_cylinder_problem(self) -> MathProblem:
        problem, solution = mathgen.volume_cylinder()
        return MathProblem("Middle School", "Geometry & Measurement", "Volume of a Cylinder", problem, str(solution))

    def generate_volume_sphere_problem(self) -> MathProblem:
        problem, solution = mathgen.volume_sphere()
        return MathProblem("Middle School", "Geometry & Measurement", "Volume of a Sphere", problem, str(solution))

    # 🏷️ Probability & Statistics
    def generate_mean_median_problem(self) -> MathProblem:
        problem, solution = mathgen.mean_median()
        return MathProblem("Middle School", "Probability & Statistics", "Mean & Median", problem, str(solution))

    def generate_combinations_problem(self) -> MathProblem:
        problem, solution = mathgen.combinations()
        return MathProblem("Middle School", "Probability & Statistics", "Combinations", problem, str(solution))

    def generate_permutation_problem(self) -> MathProblem:
        problem, solution = mathgen.permutation()
        return MathProblem("Middle School", "Probability & Statistics", "Permutation", problem, str(solution))

    def generate_dice_sum_probability_problem(self) -> MathProblem:
        problem, solution = mathgen.dice_sum_probability()
        return MathProblem("Middle School", "Probability & Statistics", "Dice Sum Probability", problem, str(solution))
