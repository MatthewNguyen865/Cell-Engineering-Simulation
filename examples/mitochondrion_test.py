from cell_simulation.utils import config as cfg
from cell_simulation.state.cell_state import CellState
from cell_simulation.organelles.mitochondrion import Mitochondrion
from cell_simulation.core.simulation import Simulation

cell_state = CellState(cfg.INITIAL_SPECIES)

mitochondrion = Mitochondrion()

simulation = Simulation(
    cell_state,
    timestep=cfg.TIME_STEP,
    organelles=[mitochondrion]
)

print("Before:")
print("Pyruvate:", cell_state.cytoplasm.get_species("pyruvate"))
print("Oxygen:", cell_state.cytoplasm.get_species("oxygen"))
print("ADP:", cell_state.cytoplasm.get_species("ADP"))
print("ATP:", cell_state.cytoplasm.get_species("ATP"))
print("CO2:", cell_state.cytoplasm.get_species("carbon_dioxide"))

simulation.run(1.0)

print("\nAfter:")
print("Pyruvate:", cell_state.cytoplasm.get_species("pyruvate"))
print("Oxygen:", cell_state.cytoplasm.get_species("oxygen"))
print("ADP:", cell_state.cytoplasm.get_species("ADP"))
print("ATP:", cell_state.cytoplasm.get_species("ATP"))
print("CO2:", cell_state.cytoplasm.get_species("carbon_dioxide"))