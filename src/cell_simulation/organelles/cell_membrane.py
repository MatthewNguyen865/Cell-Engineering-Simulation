from cell_simulation.transport.diffusion import diffusion_rate

class CellMembrane:
    """
    Models transport across the cell membrane.
    """

    def __init__(self, environment):
        self.environment = environment

        self.permeabilities = {
            "glucose": 0.01,
            "oxygen": 0.02,
        }

    def update(self, cell_state, timestep):
       for species, permeability in self.permeabilities.items():
           outside = self.environment.species[species]
           inside = cell_state.get_species(species)

           rate = diffusion_rate(
               outside,
               inside,
               permeability
           )

           change = rate * timestep

           cell_state.update_species(
               species,
               change
           )