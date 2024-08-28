import matplotlib.pyplot as plt
import numpy as np

class PSO:
    def __init__(self, num_particles, dimensions, bounds, iterations):
        self.num_particles = num_particles
        self.dimensions = dimensions
        self.bounds = bounds
        self.iterations = iterations
        self.positions = np.random.uniform(bounds[0], bounds[1], (num_particles, dimensions))
        self.velocities = np.random.uniform(-1, 1, (num_particles, dimensions))
        self.best_positions = self.positions.copy()
        self.best_global_position = self.positions[np.random.choice(num_particles)]
        self.best_global_fitness = float('inf')

    def evaluate(self, position):
        return np.sum(position**2)

    def update(self):
        for i in range(self.num_particles):
            fitness = self.evaluate(self.positions[i])
            if fitness < self.evaluate(self.best_positions[i]):
                self.best_positions[i] = self.positions[i]
            if fitness < self.best_global_fitness:
                self.best_global_position = self.positions[i]
                self.best_global_fitness = fitness

        for i in range(self.num_particles):
            inertia = 0.5 * self.velocities[i]
            cognitive = 0.8 * np.random.random() * (self.best_positions[i] - self.positions[i])
            social = 0.9 * np.random.random() * (self.best_global_position - self.positions[i])
            self.velocities[i] = inertia + cognitive + social
            self.positions[i] += self.velocities[i]

    def optimize(self):
        for _ in range(self.iterations):
            self.update()

def plot_new_method_results(new_data):
    plt.figure(figsize=(20, 15))
    
    # Detection Time
    plt.subplot(3, 2, 1)
    plt.plot(new_data['detection_times'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Simulation Step')
    plt.ylabel('Time (s)')
    plt.title('Detection Time Over Simulation Steps')
    plt.legend()
    plt.grid(True)
    
    # Accuracy
    plt.subplot(3, 2, 2)
    plt.plot(new_data['accuracies'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Simulation Step')
    plt.ylabel('Accuracy (%)')
    plt.title('Accuracy Over Simulation Steps')
    plt.legend()
    plt.grid(True)
    
    # Coverage Efficiency
    plt.subplot(3, 2, 3)
    plt.plot(new_data['coverage_efficiencies'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Simulation Step')
    plt.ylabel('Coverage Efficiency (%)')
    plt.title('Coverage Efficiency Over Simulation Steps')
    plt.legend()
    plt.grid(True)
    
    # Response Time
    plt.subplot(3, 2, 4)
    plt.plot(new_data['response_times'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Simulation Step')
    plt.ylabel('Time (s)')
    plt.title('Response Time Over Simulation Steps')
    plt.legend()
    plt.grid(True)
    
    # Scalability - Detection Time
    plt.subplot(3, 2, 5)
    plt.plot(new_data['scalability_data']['num_uavs'], new_data['scalability_data']['avg_detection_times'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Number of UAVs')
    plt.ylabel('Average Detection Time (s)')
    plt.title('Scalability - Detection Time')
    plt.legend()
    plt.grid(True)
    
    # Scalability - Response Time
    plt.subplot(3, 2, 6)
    plt.plot(new_data['scalability_data']['num_uavs'], new_data['scalability_data']['avg_response_times'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Number of UAVs')
    plt.ylabel('Average Response Time (s)')
    plt.title('Scalability - Response Time')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage of PSO
    pso = PSO(num_particles=10, dimensions=2, bounds=(-10, 10), iterations=100)
    pso.optimize()
    
    # Example data for plotting
    new_data = {
        'detection_times': [4, 3, 2, 1, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 4.5, 4.0, 3.6, 3.2, 2.8, 2.4, 2.0, 1.6, 1.2, 0.8],
        'accuracies': [91, 93, 94, 96, 97, 98, 98.5, 99, 99.2, 99.5, 89, 91, 93, 95, 96, 97, 98, 98.5, 99, 99.5],
        'coverage_efficiencies': [82, 87, 92, 97, 98, 98.5, 99, 99.2, 99.5, 99.8, 78, 82, 86, 90, 92, 94, 96, 97, 98, 99],
        'response_times': [2.5, 2, 1.5, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 3.0, 2.6, 2.2, 1.8, 1.4, 1.0, 0.8, 0.6, 0.4, 0.2],
        'scalability_data': {
            'num_uavs': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
            'avg_detection_times': [4, 3, 2, 1, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 4.5, 4.0, 3.6, 3.2, 2.8, 2.4, 2.0, 1.6, 1.2, 0.8],
            'avg_response_times': [2.5, 2, 1.5, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 3.0, 2.6, 2.2, 1.8, 1.4, 1.0, 0.8, 0.6, 0.4, 0.2]
        }
    }

    plot_new_method_results(new_data)