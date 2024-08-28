import matplotlib.pyplot as plt
import numpy as np

print("Script is running...")

def measure_detection_time(fire_start_time, detection_time):
    return detection_time - fire_start_time

def calculate_accuracy(true_positives, false_positives, false_negatives, true_negatives):
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    accuracy = (true_positives + true_negatives) / (true_positives + true_negatives + false_positives + false_negatives)
    return precision, recall, accuracy

def calculate_coverage(total_area, covered_area):
    return (covered_area / total_area) * 100

def measure_response_time(detection_time, response_time):
    return response_time - detection_time 

def measure_scalability_performance(num_uavs, detection_times, response_times):
    avg_detection_time = sum(detection_times) / len(detection_times)
    avg_response_time = sum(response_times) / len(response_times)
    return avg_detection_time, avg_response_time

def plot_results(detection_times, accuracies, coverage_efficiencies, response_times, scalability_data):
    plt.figure(figsize=(20, 15))
    
    # Detection Time
    plt.subplot(3, 2, 1)
    plt.plot(detection_times, marker='o', linestyle='-', color='b', label='Detection Time')
    plt.xlabel('Simulation Step')
    plt.ylabel('Time (s)')
    plt.title('Detection Time Over Simulation Steps')
    plt.legend()
    
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example data
    detection_times = [5, 4, 3, 2]
    accuracies = [90, 92, 93, 95]
    coverage_efficiencies = [80, 85, 90, 95]
    response_times = [3, 2.5, 2, 1.5]
    scalability_data = {
        'num_uavs': [5, 10, 15, 20],
        'avg_detection_times': [5, 4, 3, 2],
        'avg_response_times': [3, 2.5, 2, 1.5]
    }

    plot_results(detection_times, accuracies, coverage_efficiencies, response_times, scalability_data)