from cell_simulation.utils import config as cfg

class ER:
    """
    Models folding of proteins
    """

    def __init__(self):
        pass

    def update(self, cell_state, timestep):
        cytoplasm = cell_state.cytoplasm

        unfolded_proteins = cytoplasm.get_species("unfolded_proteins")
        ATP = cytoplasm.get_species("ATP")

        rate = cfg.PROTEIN_FOLDING_RATE * unfolded_proteins * ATP
        reaction_amount = rate * timestep
        reaction_amount = min(
            reaction_amount,
            unfolded_proteins,
            ATP
        )

        cytoplasm.update_species("unfolded_proteins", -reaction_amount)
        cytoplasm.update_species("ATP", -reaction_amount)
        cytoplasm.update_species("ADP", reaction_amount)
        cytoplasm.update_species("proteins", reaction_amount)