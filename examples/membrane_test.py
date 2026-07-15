from cell_simulation.state.cell_state import CellState
from cell_simulation.state.cell_environment import Environment
from cell_simulation.organelles.cell_membrane import CellMembrane
from cell_simulation.utils import config as cfg
from cell_simulation.core.simulation import Simulation

environment = Environment()
cell_state = CellState(cfg.INITIAL_SPECIES)
cell_membrane = CellMembrane(environment)

print("Before transport:")
print("Glucose:", cell_state.cytoplasm.get_species("glucose"))
print("Oxygen:", cell_state.cytoplasm.get_species("oxygen"))

simulation = Simulation(
    cell_state,
    timestep=0.1,
    organelles=[cell_membrane]
)
simulation.run(1.0)

print("\nAfter transport:")
print("Glucose:", cell_state.cytoplasm.get_species("glucose"))
print("Oxygen:", cell_state.cytoplasm.get_species("oxygen"))