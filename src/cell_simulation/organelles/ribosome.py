from cell_simulation.utils import config as cfg

class Ribosome:
    """
    Models simplified protein synthesis
    """

    def __init__(self):
        pass

    def update(self, cell_state, timestep):
        cytoplasm = cell_state.cytoplasm
        
        mRNA = cytoplasm.get_species("mRNA")
        amino_acids = cytoplasm.get_species("amino_acids")
        ATP = cytoplasm.get_species("ATP")

        rate = cfg.TRANSLATION_RATE * mRNA * amino_acids * ATP
        reaction_amount = rate * timestep
        reaction_amount = min(
            reaction_amount,
            amino_acids,
            ATP
        )

        cytoplasm.update_species("amino_acids", -reaction_amount)
        cytoplasm.update_species("ATP", -reaction_amount)
        cytoplasm.update_species("proteins", reaction_amount)

