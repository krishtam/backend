from services.math_service import GeneralMathService  
from models.db import get_db
from sqlalchemy.orm import Session
from models.user import User
from models.math_problem import MathProblem

class QuizService:
    """Manages quiz functionality including generating quizzes, submitting answers, and awarding points/currency."""

    @staticmethod
    def get_quiz_problems(grade_level: str, category: str, topics: list):
        """Fetches a set of problems based on the user's requested topics."""
        problems = []
        for topic in topics:
            try:
                problem = GeneralMathService.generate_problem(grade_level, category, topic)
                problems.append(problem)
            except ValueError as e:
                print(f"Error: {e}")
        return problems

    @staticmethod
    def submit_quiz(user_id: int, answers: list):
        """
        Submits a quiz, checks answers, calculates score, and awards points/currency.
        
        Args:
            user_id (int): The ID of the user submitting the quiz.
            answers (list): List of dictionaries with {"problem": str, "user_answer": str}.

        Returns:
            dict: Summary of quiz performance including score and rewards.
        """
        db: Session = get_db()
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return {"error": "User not found."}

        correct_count = 0
        total_questions = len(answers)

        for answer in answers:
            generated_problem = GeneralMathService.generate_problem("Unknown", "Unknown", answer["problem"])
            
            if generated_problem.solution.strip() == answer["user_answer"].strip():
                correct_count += 1

        # Calculate rewards
        score_percentage = (correct_count / total_questions) * 100
        points_earned = correct_count * 10  # Example: 10 points per correct answer
        currency_earned = correct_count * 5  # Example: 5 in-game currency per correct answer

        # Update user stats
        user.quiz_points += points_earned
        user.in_game_currency += currency_earned
        db.commit()

        return {
            "total_questions": total_questions,
            "correct_answers": correct_count,
            "score_percentage": score_percentage,
            "points_earned": points_earned,
            "currency_earned": currency_earned
        }
