import matplotlib.pyplot as plt
import numpy as np

def plot_results(existing_data, new_data):
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
    
    # Scalability Performance
    plt.subplot(3, 2, 5)
    plt.plot(existing_data['scalability_data']['num_uavs'], existing_data['scalability_data']['avg_detection_times'], marker='o', linestyle='-', color='b', label='Existing Method Detection Time')
    plt.plot(new_data['scalability_data']['num_uavs'], new_data['scalability_data']['avg_detection_times'], marker='x', linestyle='--', color='r', label='New Method Detection Time')
    plt.plot(existing_data['scalability_data']['num_uavs'], existing_data['scalability_data']['avg_response_times'], marker='o', linestyle='-', color='g', label='Existing Method Response Time')
    plt.plot(new_data['scalability_data']['num_uavs'], new_data['scalability_data']['avg_response_times'], marker='x', linestyle='--', color='m', label='New Method Response Time')
    plt.xlabel('Number of UAVs')
    plt.ylabel('Time (s)')
    plt.title('Scalability Performance')
    plt.legend()
    plt.grid(True)
    
    # Table for Summary
    plt.subplot(3, 2, 6)
    cell_text = [
        ['Detection Time', np.mean(existing_data['detection_times']), np.mean(new_data['detection_times'])],
        ['Accuracy', np.mean(existing_data['accuracies']), np.mean(new_data['accuracies'])],
        ['Coverage Efficiency', np.mean(existing_data['coverage_efficiencies']), np.mean(new_data['coverage_efficiencies'])],
        ['Response Time', np.mean(existing_data['response_times']), np.mean(new_data['response_times'])],
        ['Avg Detection Time (Scalability)', np.mean(existing_data['scalability_data']['avg_detection_times']), np.mean(new_data['scalability_data']['avg_detection_times'])],
        ['Avg Response Time (Scalability)', np.mean(existing_data['scalability_data']['avg_response_times']), np.mean(new_data['scalability_data']['avg_response_times'])]
    ]
    columns = ('Metric', 'Existing Method', 'New Method')
    plt.table(cellText=cell_text, colLabels=columns, loc='center')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example data for existing method
    existing_data = {
        'detection_times': [5, 4, 3, 2],
        'accuracies': [90, 92, 93, 95],
        'coverage_efficiencies': [80, 85, 90, 95],
        'response_times': [3, 2.5, 2, 1.5],
        'scalability_data': {
            'num_uavs': [5, 10, 15, 20],
            'avg_detection_times': [5, 4, 3, 2],
            'avg_response_times': [3, 2.5, 2, 1.5]
        }
    }

    # Example data for new method
    new_data = {
        'detection_times': [4, 3, 2, 1],
        'accuracies': [91, 93, 94, 96],
        'coverage_efficiencies': [82, 87, 92, 97],
        'response_times': [2.5, 2, 1.5, 1],
        'scalability_data': {
            'num_uavs': [5, 10, 15, 20],
            'avg_detection_times': [4, 3, 2, 1],
            'avg_response_times': [2.5, 2, 1.5, 1]
        }
    }

    plot_results(existing_data, new_data)