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
    "unfolded_proteins": 0.0,
    "proteins": 0.0,
    "packaged_proteins": 0.0,
    "damaged_proteins": 0.0,
    "mRNA": 0.0
}

# Numerical settings
SOLVER_METHOD = "RK45"

# Cytoplasmic settings
CYTOPLASM_VOLUME = 1.0e-15      # m^3 or choose consistent units
CYTOPLASM_TEMPERATURE = 310.15  # K

# Mitochondrion settings
MITOCHONDRIAL_RATE_CONSTANT = 0.05
MITOCHONDRIAL_ATP_YIELD = 1.0

# Nucleus settings
TRANSCRIPTION_RATE = 0.01

# Ribosome settings
TRANSLATION_RATE = 0.02
PROTEIN_YIELD = 1.0

# Endoplasmic Reticulum settings
PROTEIN_FOLDING_RATE = 0.02

# Golgi Apparatus settings
PROTEIN_PACKAGING_RATE = 0.02

# Lysosome settings
LYSOSOME_DEGRADATION_RATE = 0.02

# Glycolysis settings
GLYCOLYSIS_RATE_CONSTANT = 0.03
GLYCOLYSIS_ATP_YIELD = 2.0