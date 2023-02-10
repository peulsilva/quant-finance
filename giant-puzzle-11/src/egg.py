class Egg():
    def __init__(self, highest_floor : int) -> None:
        self.highest_floor = highest_floor
        self.broken = False
    
    def throw(self, floor):
        if floor > self.highest_floor:
            self.broken = True
    
    def is_broken(self):
        return self.broken