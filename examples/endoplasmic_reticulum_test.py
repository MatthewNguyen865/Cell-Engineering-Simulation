from cell_simulation.utils import config as cfg
from cell_simulation.state.cell_state import CellState
from cell_simulation.organelles.ribosome import Ribosome
from cell_simulation.organelles.nucleus import Nucleus
from cell_simulation.organelles.endoplasmic_reticulum import ER
from cell_simulation.core.simulation import Simulation

cell_state = CellState(cfg.INITIAL_SPECIES)

simulation = Simulation(
    cell_state=cell_state,
    timestep=cfg.TIME_STEP,
    organelles=[Nucleus(), Ribosome(), ER()]
)

print("Before:")
print("mRNA:", cell_state.cytoplasm.get_species("mRNA"))
print("Unfolded proteins:", cell_state.cytoplasm.get_species("unfolded_proteins"))
print("Proteins:", cell_state.cytoplasm.get_species("proteins"))
print("ATP:", cell_state.cytoplasm.get_species("ATP"))

simulation.run(1.0)

print("\nAfter:")
print("mRNA:", cell_state.cytoplasm.get_species("mRNA"))
print("Unfolded proteins:", cell_state.cytoplasm.get_species("unfolded_proteins"))
print("Proteins:", cell_state.cytoplasm.get_species("proteins"))
print("ATP:", cell_state.cytoplasm.get_species("ATP"))