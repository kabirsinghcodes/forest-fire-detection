# pso.py
import numpy as np

class PSO:
    def __init__(self, num_particles, dimensions, bounds, iterations):
        self.num_particles = num_particles
        self.dimensions = dimensions
        self.bounds = bounds
        self.iterations = iterations
        self.particles = np.random.rand(num_particles, dimensions) * (bounds[1] - bounds[0]) + bounds[0]
        self.velocities = np.random.rand(num_particles, dimensions)
        self.best_positions = self.particles.copy()
        self.global_best_position = self.best_positions[np.argmin(self.evaluate(self.best_positions))]

    def evaluate(self, positions):
        # Define the objective function here
        return np.sum(positions**2, axis=1)

    def update(self):
        for i in range(self.iterations):
            fitness = self.evaluate(self.particles)
            better_fit = fitness < self.evaluate(self.best_positions)
            self.best_positions[better_fit] = self.particles[better_fit]
            self.global_best_position = self.best_positions[np.argmin(self.evaluate(self.best_positions))]
            self.velocities = 0.5 * self.velocities + 0.5 * (self.best_positions - self.particles) + 0.5 * (self.global_best_position - self.particles)
            self.particles += self.velocities

# Example usage
pso = PSO(num_particles=10, dimensions=2, bounds=(-10, 10), iterations=100)
pso.update()
print("Global Best Position:", pso.global_best_position)