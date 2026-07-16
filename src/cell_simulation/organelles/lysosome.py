from cell_simulation.utils import config as cfg

class Lysosome:
    """
    Models degradation and recycling of damaged proteins.
    """

    def __init__(self):
        pass

    def update(self, cell_state, timestep):
        cytoplasm = cell_state.cytoplasm

        damaged_proteins = cytoplasm.get_species("damaged_proteins")
        ATP = cytoplasm.get_species("ATP")

        rate = cfg.LYSOSOME_DEGRADATION_RATE * damaged_proteins * ATP
        reaction_amount = rate * timestep
        reaction_amount = min(
            reaction_amount,
            damaged_proteins,
            ATP
        )

        cytoplasm.update_species("damaged_proteins", -reaction_amount)
        cytoplasm.update_species("ATP", -reaction_amount)
        cytoplasm.update_species("amino_acids", reaction_amount)