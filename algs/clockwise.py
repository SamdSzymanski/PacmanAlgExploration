class Clockwise():
    
    game = None

    def setup(self):
        pass
    
    def get_dir(self):
        poss_moves = self.game.pacman.allowed_moves
        current_dir = self.game.pacman.direction
        clockwise_dirs = ["up", "right", "down", "left"]
        for direction in clockwise_dirs:
            next_dir_index = (clockwise_dirs[current_dir + 1] % 4) 
            #%4 will make it so "left" + 1 points to "up" instead of throwing an error
            next_dir = clockwise_dirs[next_dir_index]
            if direction == current_dir and next_dir in poss_moves:
                current_dir = next_dir
            else:
                continue
        return current_dir
        #Need to make code that makes sure p

                

    
            
