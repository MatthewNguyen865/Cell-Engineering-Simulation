from cell_simulation.compartments.cytoplasm import Cytoplasm

class CellState:
    """
    Stores the current state of the simulated cell.
    """

    def __init__(self, initial_species):
        self.time = 0.0
        self.cytoplasm = Cytoplasm(initial_species)