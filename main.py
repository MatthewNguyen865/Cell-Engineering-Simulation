from src.cell_simulation.state.cell_state import CellState
from src.cell_simulation.core.simulation import Simulation
from src.cell_simulation.utils import config as cfg

cell = CellState(cfg.INITIAL_SPECIES)

simulation = Simulation(
    cell_state=cell,
    timestep=cfg.TIME_STEP
)

simulation.run(cfg.SIMULATION_TIME)

print(cell.time)
print(cell.cytoplasm.species)