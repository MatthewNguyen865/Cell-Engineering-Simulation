"""
Global configuration parameters for the cell simulation.
"""

# Simulation settings
TIME_STEP = 0.1
SIMULATION_TIME = 100.0

# Cell properties
CELL_VOLUME = 1.0  # arbitrary volume units
INITIAL_TEMPERATURE = 310.15  # Kelvin

# Initial species concentrations
INITIAL_SPECIES = {
    "glucose": 5.0,
    "oxygen": 0.2,
    "carbon_dioxide": 0.0,
    "ATP": 1.0,
    "ADP": 1.0,
    "pyruvate": 5.0,
    "amino_acids": 1.0,
    "proteins": 0.0,
}

# Numerical settings
SOLVER_METHOD = "RK45"

# Cytoplasmic settings
CYTOPLASM_VOLUME = 1.0e-15      # m^3 or choose consistent units
CYTOPLASM_TEMPERATURE = 310.15  # K

# Mitochondrion settings
MITOCHONDRIAL_RATE_CONSTANT = 0.05
MITOCHONDRIAL_ATP_YIELD = 1.0