import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        """
            Internal function
            It changes the direction of a specif Snake
            It is written here to be reused
        """
        def execute_snake_action(x, y, snake):
            self._direction = Point(x, y)
            snake.turn_head(self._direction)

        # snake1 is the RedSnake and snake2 is the GreenSnake
        snake1 = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")

        # the following lines consider all possible keys and execute actions according to the player
        
        # left
        if self._keyboard_service.is_key_down('a'):
            execute_snake_action(-constants.CELL_SIZE, 0, snake1)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            execute_snake_action(constants.CELL_SIZE, 0, snake1)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            execute_snake_action(0, -constants.CELL_SIZE, snake1)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            execute_snake_action(0, constants.CELL_SIZE, snake1)
        
        # left
        if self._keyboard_service.is_key_down('j'):
            execute_snake_action(-constants.CELL_SIZE, 0, snake2)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            execute_snake_action(constants.CELL_SIZE, 0, snake2)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            execute_snake_action(0, -constants.CELL_SIZE, snake2)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            execute_snake_action(0, constants.CELL_SIZE, snake2)

    