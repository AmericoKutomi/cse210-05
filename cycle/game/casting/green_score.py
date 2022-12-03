import constants
from game.casting.actor import Actor
from game.casting.score import Score
from game.shared.point import Point


class GreenScore(Score):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        # the inherited __init__ is called first
        super().__init__()

        # the position is specific to the GreenSnake: at the right part of the first line
        self._position = Point(constants.MAX_X - 150, 0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        # the inherited add_points is called first
        super().add_points(points)

        # then, the text is changed to a specific one
        self.set_text(f"Player Two: {self._points}")