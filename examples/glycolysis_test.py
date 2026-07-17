from cell_simulation.utils import config as cfg
from cell_simulation.state.cell_state import CellState
from cell_simulation.core.simulation import Simulation
from cell_simulation.processes.glycolysis import Glycolysis

cell_state = CellState(cfg.INITIAL_SPECIES)

simulation = Simulation(
    cell_state=cell_state,
    timestep=cfg.TIME_STEP,
    organelles=[Glycolysis()]
)

print("Before:")
print("Glucose:", cell_state.cytoplasm.get_species("glucose"))
print("Pyruvate:", cell_state.cytoplasm.get_species("pyruvate"))
print("ATP:", cell_state.cytoplasm.get_species("ATP"))
print("ADP:", cell_state.cytoplasm.get_species("ADP"))

simulation.run(1.0)

print("\nAfter:")
print("Glucose:", cell_state.cytoplasm.get_species("glucose"))
print("Pyruvate:", cell_state.cytoplasm.get_species("pyruvate"))
print("ATP:", cell_state.cytoplasm.get_species("ATP"))
print("ADP:", cell_state.cytoplasm.get_species("ADP"))