# Cell Simulation

A modular Python-based engineering simulation of a simplified eukaryotic cell, modeling matter and energy exchange between cellular components through mathematical processes over time.

## Overview

Cell Simulation is an extensible computational model designed to simulate the behavior of a simplified eukaryotic cell. The project models how cellular components interact by exchanging molecular species and energy through mathematically represented biological processes.

The simulation uses a modular architecture where each cellular component is represented as an independent software module. Components communicate through a shared cellular state and update the system sequentially over discrete time steps.

Version 1.0.0 establishes the foundation of the simulation by implementing:

- Membrane transport
- Cellular metabolism
- Energy production and recycling
- Gene expression
- Protein synthesis and processing
- Protein degradation and recycling

The goal of this project is not to recreate every biological detail of a living cell, but to create an engineering-focused framework that can be expanded with additional biological complexity in future releases.

For a detailed explanation of the software architecture and design decisions, see:

[Architecture Documentation](docs/architecture.md)

---

# Features

## Cellular Components

- **Cell membrane transport**
  - Models movement of extracellular glucose and oxygen into the cell through diffusion.

- **Cytoplasm state management**
  - Stores and tracks molecular species, cellular conditions, and simulation state.

- **Mitochondrion**
  - Models simplified ATP production using pyruvate and oxygen.
  - Produces carbon dioxide as a metabolic byproduct.

- **Nucleus**
  - Models simplified transcription and mRNA production.

- **Ribosome**
  - Models protein synthesis using mRNA, amino acids, and ATP.

- **Endoplasmic Reticulum**
  - Models simplified protein folding.

- **Golgi Apparatus**
  - Models protein modification and packaging.

- **Lysosome**
  - Models degradation of damaged proteins and recycling of amino acids.

---

## Metabolic Processes

- **Membrane nutrient transport**
  - Allows extracellular glucose and oxygen to enter the cell.

- **Glycolysis**
  - Converts glucose into pyruvate.
  - Produces ATP from ADP to support cellular energy requirements.

- **ATP/ADP energy cycle**
  - Connects energy-producing and energy-consuming processes to maintain cellular metabolism.

---

## Software Design

- Modular component-based architecture
- Sequential simulation updates
- Configurable simulation parameters
- Separation between:
  - Simulation control
  - Cellular state management
  - Biological components
  - Configuration settings
- Extensible framework for adding future biological processes

# Project Structure

```text
cell-simulation/
│
├── src/
│   └── cell_simulation/
│       ├── core/
│       │   └── simulation.py
│       │
│       ├── organelles/
│       │   ├── cell_membrane.py
│       │   ├── mitochondrion.py
│       │   ├── nucleus.py
│       │   ├── ribosome.py
│       │   ├── endoplasmic_reticulum.py
│       │   ├── golgi.py
│       │   └── lysosome.py
│       │
│       ├── processes/
│       │   └── glycolysis.py
│       │
│       ├── state/
│       │   ├── cell_state.py
│       │   ├── cytoplasm.py
│       │   └── cell_environment.py
│       │
│       └── utils/
│           └── config.py
│
├── examples/
|   ├── endoplasmic_reticulum_test.py
|   ├── glycolysis_test.py
|   ├── golgi_test.py
|   ├── lysosome_test.py
|   ├── membrane_test.py
|   ├── mitochondrion_test.py
|   ├── nucleus_test.py
|   ├── ribosome_test.py
│   └── full_cell_simulation.py
│
├── docs/
│   └── architecture.md
│
├── tests/
│
├── requirements.txt
└── README.md
```

The project is organized into separate modules based on responsibility:

- `core/` contains the simulation engine that controls time advancement and component updates.
- `organelles/` contains models of cellular structures responsible for specific biological functions.
- `processes/` contains metabolic processes that do not represent physical organelles.
- `state/` manages the cellular environment and shared molecular state.
- `utils/` contains configuration parameters used throughout the simulation.
- `examples/` contains demonstration scripts showing how to use the simulator.
- `docs/` contains technical documentation describing architecture and design decisions.
- `tests/` contains validation scripts for individual components and processes.

# Installation

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.13 or later
- pip (Python package installer)

## Clone the Repository

```bash
git clone https://github.com/MatthewNguyen865/Cell-Engineering-Simulation.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Project
```bash
python main.py
```

---

# Usage

## Full Cell Simulation

Run the integrated cell simulation example:

```bash
python examples/full_cell_simulation.py
```

This example initializes a simplified eukaryotic cell and simulates the interaction between membrane transport, metabolism, energy production, gene expression, protein synthesis, protein processing, and protein recycling.

The simulation prints the cellular state at multiple time points, allowing changes in molecular species to be observed throughout the simulation.

---

## Individual Component Examples

The `examples/` directory also contains standalone examples demonstrating the behavior of individual cellular components and biological processes, including:

- Cell membrane transport
- Glycolysis
- Mitochondrion
- Nucleus
- Ribosome
- Endoplasmic reticulum
- Golgi apparatus
- Lysosome

These examples can be run individually using Python. For example:

```bash
python examples/mitochondrion_test.py
```

Each example demonstrates the behavior of a single component in isolation, making it easier to understand and validate individual parts of the simulation.

---

# Example Output

Running the full cell simulation produces output similar to the following:

```text
Initial State (t = 0.00):
Glucose: 1.0
Oxygen: 0.5
Carbon dioxide: 0.0
ATP: 0.5
ADP: 1.5
Pyruvate: 0.5
Amino acids: 2.0
Unfolded proteins: 0.0
Proteins: 0.0
Packaged proteins: 0.0
Damaged proteins: 0.1
mRNA: 0.0

...

Final State (t = 40.00):
Glucose: 2.944729519753472
Oxygen: 2.271299715601194
Carbon dioxide: 1.032687334022634
ATP: 2.9051148482677718
ADP: 0.36125840899827866
Pyruvate: 0.7336859232434094
Amino acids: 1.4079609084627285
Unfolded proteins: 0.37565981371217433
Proteins: 0.18883352491363414
Packaged proteins: 0.1086344724147441
Damaged proteins: 0.01891128049671923
mRNA: 0.4000000000000003
```

The simulation demonstrates how molecular species change over time as nutrients enter the cell, metabolic pathways generate energy, gene expression produces proteins, and cellular components interact through a shared cellular state.

---

# Model Overview

The simulation models a simplified eukaryotic cell as a collection of independent components that interact through a shared cellular state. During each simulation step, every component reads the current state of the cell, performs its biological function, and updates the concentrations of relevant molecular species.

The overall flow of the simulation is illustrated below:

```text
                 Environment
                      │
                      ▼
              Cell Membrane
              |        │
        Glucose      Oxygen
             │          │
             ▼          │
         Glycolysis     │
             │          │
      Pyruvate      ATP Production
             │          ▲
             ▼          │
        Mitochondrion ──┘
             │
             ▼
     Carbon Dioxide + ATP
             │
             ▼
          Nucleus
             │
             ▼
            mRNA
             │
             ▼
          Ribosome
             │
             ▼
   Unfolded Proteins ⯇─────────────┐
             │                      |
             ▼                      |
   Endoplasmic Reticulum            |
             │                      |
             ▼                      |
         Proteins                   |
             │                      |
             ▼                      |
     Golgi Apparatus                |
             │                      |
             ▼                      |
   Packaged Proteins                |
          │                         |
          ▼                         |
Damaged Proteins                    |
        │                           |
        ▼                           |
    Lysosome                        |
        │                           |
        ▼                           |
   Amino Acids ───────────────┐     |
                              │     |
                              ▼     |
                         Ribosome ──┘
```

This modular design allows each biological component to be developed, tested, and extended independently while interacting through a common cellular state. As additional organelles and biochemical pathways are introduced in future releases, they can be incorporated into the existing simulation framework with minimal changes to the overall architecture.

---

# Design Decisions

## Sequential Component Updates

The simulation uses a sequential update strategy rather than a synchronous update strategy. During each simulation step, every component updates the shared cellular state in a predefined order.

This approach allows downstream components to immediately use products generated by upstream components within the same simulation step. For example, glycolysis produces pyruvate before the mitochondrion consumes it to produce ATP.

The sequential update model was chosen because it produces deterministic and reproducible simulation behavior while maintaining a simple and modular implementation.

---

## Completing the Energy Cycle

During development of Version 1.0.0, it became apparent that the original model contained an incomplete energy cycle. While nutrients entered the cell and ATP was consumed by several processes, there was no mechanism to convert glucose into pyruvate or regenerate ATP from ADP.

To address this, glycolysis was introduced before the initial release. This addition allowed the simulation to:

- Consume glucose
- Produce pyruvate
- Convert ADP into ATP
- Sustain mitochondrial ATP production

This design change established a complete simplified energy cycle and ensured that the simulated cell could maintain its metabolism over time rather than exhausting its available energy.

---

# Future Improvements

Future releases of Cell Simulation are planned to expand both the biological realism and engineering capabilities of the simulator. Potential enhancements include:

## Biological Features

- Citric acid (Krebs) cycle
- Electron transport chain and oxidative phosphorylation
- Lipid metabolism
- DNA replication
- Cell division (mitosis)
- Protein secretion and exocytosis
- Cell signaling pathways
- Additional organelles (e.g., peroxisomes, vacuoles)

## Simulation Features

- Additional molecular species and reaction pathways
- Improved reaction kinetics
- Configurable simulation scenarios
- Support for multiple interacting cells
- Enhanced parameter validation
- Performance optimization for larger simulations

## Visualization

- Time-series plots of molecular species
- ATP, ADP, and metabolite concentration profiles
- Cellular process visualization
- Network diagrams of molecular interactions
- Interactive simulation dashboards

## Software Improvements

- Automated unit testing
- Continuous integration workflows
- Improved API documentation
- Package distribution through PyPI
- Expanded example simulations

## Analysis and Modeling Tools

- MATLAB-based validation and numerical analysis
- Parameter estimation workflows
- Advanced sensitivity studies
- Optimization of biological model parameters

---

# Technologies and Methods

- Python 3.13
- Object-oriented programming
- Modular software architecture
- Numerical simulation methods
- Engineering-based mathematical modeling

---

# Author

Matthew Nguyen
Chemical Engineering Student
Texas A&M University