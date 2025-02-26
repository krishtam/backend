from models.db import Base, engine

# Import all models so they are registered with SQLAlchemy
from models.topic import Topic
from models.unit import Unit
from models.user import User
from models.progress import Progress
from models.leaderboard import Leaderboard
from models.inventory_item import InventoryItem
from models.user_inventory import UserInventory
from models.math_problem import MathProblem  # Make sure this is imported too

# Create all tables
Base.metadata.create_all(bind=engine)