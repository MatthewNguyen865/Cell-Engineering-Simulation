from cell_simulation.utils import config as cfg

class Glycolysis:
    """
    Models simplified glycolysis, converting glucose into pyruvate while generating ATP.
    """

    def __init__(self):
        pass

    def update(self, cell_state, timestep):
        cytoplasm = cell_state.cytoplasm

        glucose = cytoplasm.get_species("glucose")
        ADP = cytoplasm.get_species("ADP")

        rate = cfg.GLYCOLYSIS_RATE_CONSTANT * glucose * ADP
        reaction_amount = rate * timestep
        reaction_amount = min(
            reaction_amount,
            glucose,
            ADP
        )

        cytoplasm.update_species("glucose", -reaction_amount)
        cytoplasm.update_species("ADP", -reaction_amount)
        cytoplasm.update_species("pyruvate", reaction_amount)
        cytoplasm.update_species("ATP", reaction_amount * cfg.GLYCOLYSIS_ATP_YIELD)