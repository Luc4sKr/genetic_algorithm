class City:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"City({self.x}, {self.y})"