from cell_simulation.utils import config as cfg
from cell_simulation.state.cell_state import CellState
from cell_simulation.state.cell_environment import Environment
from cell_simulation.organelles.cell_membrane import CellMembrane
from cell_simulation.organelles.mitochondrion import Mitochondrion
from cell_simulation.organelles.ribosome import Ribosome
from cell_simulation.organelles.nucleus import Nucleus
from cell_simulation.organelles.endoplasmic_reticulum import ER
from cell_simulation.organelles.golgi import Golgi
from cell_simulation.processes.glycolysis import Glycolysis
from cell_simulation.organelles.lysosome import Lysosome
from cell_simulation.core.simulation import Simulation

cell_state = CellState(cfg.INITIAL_SPECIES)
cell_state.cytoplasm.set_species("glucose", 1.0)
cell_state.cytoplasm.set_species("oxygen", 0.5)
cell_state.cytoplasm.set_species("ATP", 0.5)
cell_state.cytoplasm.set_species("ADP", 1.5)
cell_state.cytoplasm.set_species("pyruvate", 0.5)
cell_state.cytoplasm.set_species("amino_acids", 2.0)
cell_state.cytoplasm.set_species("damaged_proteins", 0.1)

cell_membrane = CellMembrane(Environment())

components = [cell_membrane, Glycolysis(), Mitochondrion(), Nucleus(), Ribosome(), ER(), Golgi(), Lysosome()]
simulate = Simulation(
    cell_state=cell_state,
    timestep=cfg.TIME_STEP,
    organelles=components
)

def print_state(label, state):
    print(label)
    print("Glucose:", state.cytoplasm.get_species("glucose"))
    print("Oxygen:", state.cytoplasm.get_species("oxygen"))
    print("Carbon dioxide:", state.cytoplasm.get_species("carbon_dioxide"))
    print("ATP:", state.cytoplasm.get_species("ATP"))
    print("ADP:", state.cytoplasm.get_species("ADP"))
    print("Pyruvate:", state.cytoplasm.get_species("pyruvate"))
    print("Amino acids:", state.cytoplasm.get_species("amino_acids"))
    print("Unfolded proteins:", state.cytoplasm.get_species("unfolded_proteins"))
    print("Proteins:", state.cytoplasm.get_species("proteins"))
    print("Packaged proteins:", state.cytoplasm.get_species("packaged_proteins"))
    print("Damaged proteins:", state.cytoplasm.get_species("damaged_proteins"))
    print("mRNA:", state.cytoplasm.get_species("mRNA"))

print_state(f"Initial State (t = {cell_state.time:.2f}):", cell_state)

simulate.run(10.0)
print_state(f"\nState 1 (t = {cell_state.time:.2f}):", cell_state)

simulate.run(20.0)
print_state(f"\nState 2 (t = {cell_state.time:.2f}):", cell_state)

simulate.run(30.0)
print_state(f"\nState 3 (t = {cell_state.time:.2f}):", cell_state)

simulate.run(40.0)
print_state(f"\nFinal State (t = {cell_state.time:.2f}):", cell_state)