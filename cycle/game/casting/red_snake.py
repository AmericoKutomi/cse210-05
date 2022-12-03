import constants
from game.casting.snake import Snake
from game.shared.point import Point
from game.casting.actor import Actor

class RedSnake(Snake):
    """
    A Snake red colored
    
    A Red Snake is derived from Snake class

    Attributes:
        No specific attributes
    """
    def __init__(self):
        # the inherited __init__ is called first
        super().__init__()

    def grow_tail(self, number_of_segments):
        # the inherited grow_tail is NOT called because it is totally overridden here

        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.RED)    # a specific color is assigned to the Snake
            self._segments.append(segment)

    def _prepare_body(self):
        # the inherited _prepare_body is NOT called because it is totally overridden here

        x = int(constants.MAX_X / 6)            # the specific position of the Snake is defined here
        y = int(constants.MAX_Y / 4)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x , y + i * constants.CELL_SIZE)
            velocity = Point(0, -1 * constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            # the specific position of the Snake is defined here
            color = constants.YELLOW if i == 0 else constants.RED

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)