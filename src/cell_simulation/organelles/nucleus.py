from cell_simulation.utils import config as cfg

class Nucleus:
    """
    Models simplified DNA storage and transcription.
    """

    def __init__(self):
        self.genes = {
            "housekeeping": True
        }
    
    def update(self, cell_state, timestep):
        cytoplasm = cell_state.cytoplasm

        for gene, active in self.genes.items():
            if active:
                mRNA_produced = (cfg.TRANSCRIPTION_RATE * timestep)
                cytoplasm.update_species("mRNA", mRNA_produced)


