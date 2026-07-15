from cell_simulation.utils import config as cfg

class Golgi:
    """
    Models protein modification and packaging.
    """

    def __init__(self):
        pass

    def update(self, cell_state, timestep):
        cytoplasm = cell_state.cytoplasm

        proteins = cytoplasm.get_species("proteins")
        ATP = cytoplasm.get_species("ATP")

        rate = cfg.PROTEIN_PACKAGING_RATE * proteins * ATP
        reaction_amount = rate * timestep
        reaction_amount = min(
            reaction_amount,
            proteins,
            ATP
        )

        cytoplasm.update_species("proteins", -reaction_amount)
        cytoplasm.update_species("ATP", -reaction_amount)
        cytoplasm.update_species("packaged_proteins", reaction_amount)