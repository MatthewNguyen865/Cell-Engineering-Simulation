from cell_simulation.state.cell_state import CellState
from cell_simulation.organelles.lysosome import Lysosome
from cell_simulation.core.simulation import Simulation
from cell_simulation.utils import config as cfg

cell_state = CellState(cfg.INITIAL_SPECIES)

cell_state.cytoplasm.set_species("damaged_proteins", 1.0)

simulation = Simulation(
    cell_state=cell_state,
    timestep=cfg.TIME_STEP,
    organelles=[Lysosome()]
)

print("Before:")
print("Damaged proteins:", cell_state.cytoplasm.get_species("damaged_proteins"))
print("Amino acids:", cell_state.cytoplasm.get_species("amino_acids"))
print("ATP:", cell_state.cytoplasm.get_species("ATP"))

simulation.run(1.0)

print("\nAfter")
print("Damaged proteins:", cell_state.cytoplasm.get_species("damaged_proteins"))
print("Amino acids:", cell_state.cytoplasm.get_species("amino_acids"))
print("ATP:", cell_state.cytoplasm.get_species("ATP"))