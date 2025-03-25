from fastapi import HTTPException

class TopicService:
    def __init__(self):
        # Map topics to their corresponding levels
        self.topic_to_level = {
            # Elementary School Topics
            "Addition": "elementary",
            "Subtraction": "elementary",
            "Multiplication": "elementary",
            "Division": "elementary",
            "Absolute Difference": "elementary",
            "Fraction to Decimal": "elementary",
            "Square": "elementary",
            "Square Root": "elementary",
            "Cube Root": "elementary",
            "Factorial": "elementary",
            "Greatest Common Divisor": "elementary",
            "Prime Number Check": "elementary",
            "Composite Number Check": "elementary",
            "Compare Fractions": "elementary",
            "Fraction Multiplication": "elementary",
            "Divide Fractions": "elementary",
            "Simplify Square Root": "elementary",

            # Middle School Topics
            "Basic Algebra": "middle_school",
            "Combine Like Terms": "middle_school",
            "Expanding": "middle_school",
            "Factoring": "middle_school",
            "Linear Equations": "middle_school",
            "Simple Interest": "middle_school",
            "Compound Interest": "middle_school",
            "Distance Between Two Points": "middle_school",
            "Midpoint of Two Points": "middle_school",
            "Line Equation from Two Points": "middle_school",
            "Exponentiation": "middle_school",
            "Power of Powers": "middle_school",
            "Mean & Median": "middle_school",
            "Combinations": "middle_school",
            "Permutation": "middle_school",
            "Dice Sum Probability": "middle_school",

            # High School Topics
            "Quadratic Equation": "high_school",
            "Complex Quadratic": "high_school",
            "Logarithm": "high_school",
            "Pythagorean Theorem": "high_school",
            "Basic Trigonometry": "high_school",
            "Surface Area of Pyramid": "high_school",
            "Surface Area of Cone": "high_school",
            "Volume of Pyramid": "high_school",
            "Volume of Cone": "high_school",
            "Data Summary": "high_school",
            "Confidence Interval": "high_school",
            "Conditional Probability": "high_school",
            "Binomial Distribution": "high_school",

            # Advanced High School Topics
            "Matrix Determinant": "advanced_high_school",
            "Matrix Inversion": "advanced_high_school",
            "Matrix Multiplication": "advanced_high_school",
            "Vector Cross Product": "advanced_high_school",
            "Vector Dot Product": "advanced_high_school",
            "Complex Numbers": "advanced_high_school",
            "Derivatives": "advanced_high_school",
            "Integrals": "advanced_high_school",
        }

        # Map topics to their corresponding function names
        self.topic_to_function = {
            # Elementary School Topics
            "Addition": "generate_addition_problem",
            "Subtraction": "generate_subtraction_problem",
            "Multiplication": "generate_multiplication_problem",
            "Division": "generate_division_problem",
            "Absolute Difference": "generate_absolute_difference_problem",
            "Fraction to Decimal": "generate_fraction_to_decimal_problem",
            "Square": "generate_square_problem",
            "Square Root": "generate_square_root_problem",
            "Cube Root": "generate_cube_root_problem",
            "Factorial": "generate_factorial_problem",
            "Greatest Common Divisor": "generate_gcd_problem",
            "Prime Number Check": "generate_is_prime_problem",
            "Composite Number Check": "generate_is_composite_problem",
            "Compare Fractions": "generate_compare_fractions_problem",
            "Fraction Multiplication": "generate_fraction_multiplication_problem",
            "Divide Fractions": "generate_divide_fractions_problem",
            "Simplify Square Root": "generate_simplify_square_root_problem",

            # Middle School Topics
            "Basic Algebra": "generate_basic_algebra_problem",
            "Combine Like Terms": "generate_combine_like_terms_problem",
            "Expanding": "generate_expanding_problem",
            "Factoring": "generate_factoring_problem",
            "Linear Equations": "generate_linear_equations_problem",
            "Simple Interest": "generate_simple_interest_problem",
            "Compound Interest": "generate_compound_interest_problem",
            "Distance Between Two Points": "generate_distance_two_points_problem",
            "Midpoint of Two Points": "generate_midpoint_of_two_points_problem",
            "Line Equation from Two Points": "generate_line_equation_from_2_points_problem",
            "Exponentiation": "generate_exponentiation_problem",
            "Power of Powers": "generate_power_of_powers_problem",
            "Quotient of Power (Same Base)": "generate_quotient_of_power_same_base_problem",
            "Quotient of Power (Same Power)": "generate_quotient_of_power_same_power_problem",
            "Angle of a Regular Polygon": "generate_angle_regular_polygon_problem",
            "Third Angle of a Triangle": "generate_third_angle_of_triangle_problem",
            "Fourth Angle of a Quadrilateral": "generate_fourth_angle_of_quadrilateral_problem",
            "Sum of Polygon Angles": "generate_sum_of_polygon_angles_problem",
            "Valid Triangle Check": "generate_valid_triangle_problem",
            "Surface Area of a Cube": "generate_surface_area_cube_problem",
            "Surface Area of a Cylinder": "generate_surface_area_cylinder_problem",
            "Surface Area of a Sphere": "generate_surface_area_sphere_problem",
            "Volume of a Cube": "generate_volume_cube_problem",
            "Volume of a Cylinder": "generate_volume_cylinder_problem",
            "Volume of a Sphere": "generate_volume_sphere_problem",
            "Mean & Median": "generate_mean_median_problem",
            "Combinations": "generate_combinations_problem",
            "Permutation": "generate_permutation_problem",
            "Dice Sum Probability": "generate_dice_sum_probability_problem",

            # High School Topics
            "Quadratic Equation": "generate_quadratic_equation",
            "Complex Quadratic": "generate_complex_quadratic",
            "Logarithm": "generate_logarithm_problem",
            "Pythagorean Theorem": "generate_pythagorean_theorem",
            "Basic Trigonometry": "generate_basic_trigonometry",
            "Surface Area of Pyramid": "generate_surface_area_pyramid",
            "Surface Area of Cone": "generate_surface_area_cone",
            "Volume of Pyramid": "generate_volume_pyramid",
            "Volume of Cone": "generate_volume_cone",
            "Volume of Cone Frustum": "generate_volume_cone_frustum",
            "Volume of Hemisphere": "generate_volume_hemisphere",
            "Data Summary": "generate_data_summary",
            "Confidence Interval": "generate_confidence_interval",
            "Conditional Probability": "generate_conditional_probability",
            "Binomial Distribution": "generate_binomial_distribution",
            "System of Equations": "generate_system_of_equations_problem",
            "Distance Formula": "generate_distance_formula_problem",

            # Advanced High School Topics
            "Matrix Determinant": "generate_int_matrix_22_determinant",
            "Matrix Inversion": "generate_invert_matrix",
            "Matrix Multiplication": "generate_matrix_multiplication",
            "Vector Cross Product": "generate_vector_cross",
            "Vector Dot Product": "generate_vector_dot",
            "Orthogonal Projection": "generate_orthogonal_projection",
            "Multiply Complex Numbers": "generate_multiply_complex_numbers",
            "Complex to Polar": "generate_complex_to_polar",
            "Arithmetic Progression Sum": "generate_arithmetic_progression_sum",
            "Arithmetic Progression Term": "generate_arithmetic_progression_term",
            "Geometric Progression": "generate_geometric_progression",
            "Geometric Mean": "generate_geometric_mean",
            "Harmonic Mean": "generate_harmonic_mean",
            "Angle Between Vectors": "generate_angle_btw_vectors",
            "Degree to Radian Conversion": "generate_degree_to_rad",
            "Radian to Degree Conversion": "generate_radian_to_deg",
            "Power Rule Differentiation": "generate_power_rule_differentiation",
            "Trigonometric Differentiation": "generate_trig_differentiation",
            "Power Rule Integration": "generate_power_rule_integration",
            "Definite Integral": "generate_definite_integral",
            "Stationary Points": "generate_stationary_points",
        }

    def get_topic_level(self, topic_name: str) -> str:
        """
        Get the level (elementary, middle_school, high_school, advanced_high_school) for a given topic.
        """
        formatted_topic = " ".join(word.capitalize() for word in topic_name.replace("-", " ").split())
        
        if formatted_topic not in self.topic_to_level:
            raise HTTPException(
                status_code=404,
                detail=f"Topic '{formatted_topic}' not found. Available topics: {list(self.topic_to_level.keys())}"
            )
        
        return self.topic_to_level[formatted_topic]

    def get_function_details(self, topic_name: str) -> str:
        """
        Convert a topic name to its corresponding function name.
        Returns the function name to call
        """
        # Format the topic name (replace hyphens with spaces and capitalize words)
        formatted_topic = " ".join(word.capitalize() for word in topic_name.replace("-", " ").split())

        # Check if the topic exists
        if formatted_topic not in self.topic_to_function:
            raise HTTPException(
                status_code=404, 
                detail=f"Topic '{formatted_topic}' not found. Available topics: {list(self.topic_to_function.keys())}"
            )

        # Return the function name
        return self.topic_to_function[formatted_topic] 