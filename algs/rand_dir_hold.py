import random

class Rand_Dir_Hold():
    def __init__(self):
        self.current_direction = None

    def get_dir(self, allowed_moves):
        if self.current_direction is None or self.current_direction not in allowed_moves:
            self.current_direction = random.choice(allowed_moves)
        return self.current_direction
