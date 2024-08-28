import matplotlib.pyplot as plt
import numpy as np

def plot_comparison(existing_data, new_data):
    plt.figure(figsize=(20, 15))
    
    # Detection Time
    plt.subplot(3, 2, 1)
    plt.plot(existing_data['detection_times'], marker='o', linestyle='-', color='b', label='Existing Method')
    plt.plot(new_data['detection_times'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Simulation Step')
    plt.ylabel('Time (s)')
    plt.title('Detection Time Over Simulation Steps')
    plt.legend()
    plt.grid(True)
    
    # Accuracy
    plt.subplot(3, 2, 2)
    plt.plot(existing_data['accuracies'], marker='o', linestyle='-', color='b', label='Existing Method')
    plt.plot(new_data['accuracies'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Simulation Step')
    plt.ylabel('Accuracy (%)')
    plt.title('Accuracy Over Simulation Steps')
    plt.legend()
    plt.grid(True)
    
    # Coverage Efficiency
    plt.subplot(3, 2, 3)
    plt.plot(existing_data['coverage_efficiencies'], marker='o', linestyle='-', color='b', label='Existing Method')
    plt.plot(new_data['coverage_efficiencies'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Simulation Step')
    plt.ylabel('Coverage Efficiency (%)')
    plt.title('Coverage Efficiency Over Simulation Steps')
    plt.legend()
    plt.grid(True)
    
    # Response Time
    plt.subplot(3, 2, 4)
    plt.plot(existing_data['response_times'], marker='o', linestyle='-', color='b', label='Existing Method')
    plt.plot(new_data['response_times'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Simulation Step')
    plt.ylabel('Time (s)')
    plt.title('Response Time Over Simulation Steps')
    plt.legend()
    plt.grid(True)
    
    # Scalability - Detection Time
    plt.subplot(3, 2, 5)
    plt.plot(existing_data['scalability_data']['num_uavs'], existing_data['scalability_data']['avg_detection_times'], marker='o', linestyle='-', color='b', label='Existing Method')
    plt.plot(new_data['scalability_data']['num_uavs'], new_data['scalability_data']['avg_detection_times'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Number of UAVs')
    plt.ylabel('Average Detection Time (s)')
    plt.title('Scalability - Detection Time')
    plt.legend()
    plt.grid(True)
    
    # Scalability - Response Time
    plt.subplot(3, 2, 6)
    plt.plot(existing_data['scalability_data']['num_uavs'], existing_data['scalability_data']['avg_response_times'], marker='o', linestyle='-', color='b', label='Existing Method')
    plt.plot(new_data['scalability_data']['num_uavs'], new_data['scalability_data']['avg_response_times'], marker='x', linestyle='--', color='r', label='New Method')
    plt.xlabel('Number of UAVs')
    plt.ylabel('Average Response Time (s)')
    plt.title('Scalability - Response Time')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example existing data
    existing_data = {
        'detection_times': [5.2, 4.8, 4.5, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 5.0, 4.7, 4.4, 4.1, 3.9, 3.7, 3.5, 3.3, 3.1, 2.9],
        'accuracies': [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97],
        'coverage_efficiencies': [75, 78, 80, 82, 84, 86, 88, 90, 92, 94, 75, 78, 80, 82, 84, 86, 88, 90, 92, 94],
        'response_times': [3.5, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 3.5, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6],
        'scalability_data': {
            'num_uavs': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
            'avg_detection_times': [5.2, 4.8, 4.5, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 5.0, 4.7, 4.4, 4.1, 3.9, 3.7, 3.5, 3.3, 3.1, 2.9],
            'avg_response_times': [3.5, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 3.5, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6]
        }
    }

    # New data for comparison
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

    plot_comparison(existing_data, new_data)