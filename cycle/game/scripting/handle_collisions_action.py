import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_snake_collision(cast)                  # this part verifies if one snake collides with the other
            self._handle_segment_collision(cast)                # this part verifies if the snake collides to its own segments
            self._handle_game_over(cast)                        # this part is to verify if the game is over
   
    def _handle_snake_collision(self, cast):
        """Verifies if on snake collides with the other
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        def verify_snake_collision(snake_1, snake_2):
            # it verifies if the snake_1 collides to segments of snake_2
            # if there is a collision, then snake_1 dies
            hitted = False
            head = snake_1.get_head()
            segments = snake_2.get_segments()[1:]
            for segment in segments:
                if head.get_position().equals(segment.get_position()):  # the head hits the other snake segment
                    snake_1.set_dead()                                  # the snake is considered dead
                    hitted = True
                    break
            return hitted

        def head_to_head(snake_1, snake_2):
            # this is an enhancement: to verify if the two snakes collide their heads
            # if this happens, both die
            hitted = False
            head1 = snake_1.get_head()
            head2 = snake_2.get_head()
            if head1.get_position().equals(head2.get_position()):       # head to head collision
                snake_1.set_dead()
                snake_2.set_dead()
                hitted = True
            return hitted

        # score1, snake1 are appertaining to the RedSnake 
        # and score2, snake2 are appertaining to the GreenSnake

        score1 = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")

        snake1 = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")

        # verifies if both collide their heads
        if head_to_head(snake1, snake2):
            # it is a tie
            self._is_game_over = True
            return

        # verifies if snake1 dies
        if verify_snake_collision(snake1, snake2):
            # snake2 won
            self._is_game_over = True
            score2.add_points(1)
            return

        # verifies if snake2 dies
        if verify_snake_collision(snake2, snake1):
            # snake1 won
            self._is_game_over = True
            score1.add_points(1)
            return

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        def self_collision(snake):
            # verifies if the snake head hits its own segments
            hitted = False
            head = snake.get_segments()[0]
            segments = snake.get_segments()[1:]
            
            for segment in segments:
                if head.get_position().equals(segment.get_position()):
                    self._is_game_over = True
                    hitted = True

            return hitted

        # score1, snake1 are appertaining to the RedSnake 
        # and score2, snake2 are appertaining to the GreenSnake

        snake1 = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")

        score1 = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")

        # checks snake1
        if self_collision(snake1):
            score2.add_points(1)
        
        # checks snake2
        if self_collision(snake2):
            score1.add_points(1)

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        def snake_to_white(snake):
            # internal function to be reused
            # it turns the snake white
            snake.set_dead()
            segments = snake.get_segments()
            for segment in segments:
                segment.set_color(constants.WHITE)

            pass

        if self._is_game_over:
            # snake1 is appertaining to the RedSnake 
            # snake2 is appertaining to the GreenSnake

            snake1 = cast.get_first_actor("snakes")
            snake2 = cast.get_second_actor("snakes")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            # The game over message is treated here to be specific
            message = Actor()
            if snake1.get_dead() and snake2.get_dead():
                message.set_text("It was a draw! Game Over!")
            elif snake1.get_dead():
                message.set_text("The green player won! Game Over!")
            elif snake2.get_dead():
                message.set_text("The red player won! Game Over!")
            else:
                message.set_text("Game Over!")

            message.set_position(position)
            cast.add_actor("messages", message)

            snake_to_white(snake1)
            snake_to_white(snake2)
