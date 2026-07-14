class Simulation:
    """
    Controls execution of the cell simulation.
    """

    def __init__(self, cell_state, timestep):
        self.cell_state = cell_state
        self.timestep = timestep
        self.time_history = []

    def step(self):
        self.cell_state.time += self.timestep

    def run(self, duration):
        while self.cell_state.time < duration:
            self.step()