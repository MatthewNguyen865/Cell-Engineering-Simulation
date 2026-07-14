class CellState:
    """
    Stores the current state of the simulated cell.
    """

    def __init__(self, initial_species=None):
        self.time = 0.0

        if initial_species is None:
            self.species = {}
        else:
            self.species = initial_species.copy()
        
        self.properties = {}

    def get_species(self, name):
        return self.species.get(name, 0.0)

    def set_species(self, name, value):
        self.species[name] = value

    def update_species(self, name, change):
        self.species[name] += change