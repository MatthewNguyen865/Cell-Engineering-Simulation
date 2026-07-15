from cell_simulation.utils import config as cfg

class Cytoplasm:
    """
    Represents the intracellular fluid where metabolites are stored
    and exchanged between organelles.
    """

    def __init__(self, species, volume=cfg.CYTOPLASM_VOLUME, temperature=cfg.CYTOPLASM_TEMPERATURE):
        self.species = species.copy()
        self.volume = volume
        self.temperature = temperature

    def get_species(self, name):
        return self.species.get(name, 0.0)

    def set_species(self, name, value):
        self.species[name] = value

    def update_species(self, name, change):
        if name not in self.species:
            raise KeyError(f"Unknown species: {name}")

        self.species[name] += change