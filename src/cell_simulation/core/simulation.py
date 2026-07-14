class Simulation:
    """
    Controls execution of the cell simulation.
    """

    def __init__(self, cell_state, timestep, organelles=None):
        self.cell_state = cell_state
        self.timestep = timestep
        self.time_history = []

        if organelles is None:
            self.organelles = []
        else:
            self.organelles = organelles

    def step(self):
        for organelle in self.organelles:
            organelle.update(
                self.cell_state,
                self.timestep
            )
        
        self.cell_state.time += self.timestep
        self.record_state()

    def run(self, duration):
        while self.cell_state.time < duration:
            self.step()
    
    def record_state(self):
        self.time_history.append(self.cell_state.time)