class Environment:
    """
    Represents the external environment surounding the cell.
    """
    
    def __init__(self):
        self.species = {
            "glucose": 10.0,
            "oxygen": 5.0
        }