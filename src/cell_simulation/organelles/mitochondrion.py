from cell_simulation.utils import config as cfg

class Mitochondrion:
    """
    Models simplified mitochondrial ATP production.
    """

    def __init__(self):
        pass

    def update(self, cell_state, timestep):

        cytoplasm = cell_state.cytoplasm

        pyruvate = cytoplasm.get_species("pyruvate")
        oxygen = cytoplasm.get_species("oxygen")
        ADP = cytoplasm.get_species("ADP")

        rate = (
            cfg.MITOCHONDRIAL_RATE_CONSTANT
            * pyruvate
            * oxygen
            * ADP
        )

        reaction_amount = rate * timestep
        reaction_amount = min(
            reaction_amount,
            pyruvate,
            oxygen,
            ADP
        )
        ATP_produced = reaction_amount * cfg.MITOCHONDRIAL_ATP_YIELD

        cytoplasm.update_species("pyruvate", -reaction_amount)
        cytoplasm.update_species("oxygen", -reaction_amount)
        cytoplasm.update_species("ADP", -reaction_amount)
        cytoplasm.update_species("ATP", ATP_produced)
        cytoplasm.update_species("carbon_dioxide", reaction_amount)