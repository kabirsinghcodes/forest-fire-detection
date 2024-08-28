
# Comparison Analysis of UAV Detection Methods

This project aims to compare the performance of an existing UAV detection method with a new method using various metrics such as detection times, accuracies, coverage efficiencies, response times, and scalability.

## Project Structure

- `comparison_analysis.py`: The main script that performs the comparison analysis and plots the results.
- `README.md`: This file, providing an overview of the project.

## Data

The data used for comparison includes:

### Existing Method Data

- **Detection Times**:
  ```python
  [5.2, 4.8, 4.5, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 5.0, 4.7, 4.4, 4.1, 3.9, 3.7, 3.5, 3.3, 3.1, 2.9]
  ```

- **Accuracies**:
  ```python
  [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
  ```

- **Coverage Efficiencies**:
  ```python
  [75, 78, 80, 82, 84, 86, 88, 90, 92, 94, 75, 78, 80, 82, 84, 86, 88, 90, 92, 94]
  ```

- **Response Times**:
  ```python
  [3.5, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 3.5, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6]
  ```

- **Scalability Data**:
  - **Number of UAVs**:
    ```python
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    ```
  - **Average Detection Times**:
    ```python
    [5.2, 4.8, 4.5, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 5.0, 4.7, 4.4, 4.1, 3.9, 3.7, 3.5, 3.3, 3.1, 2.9]
    ```
  - **Average Response Times**:
    ```python
    [3.5, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 3.5, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6]
    ```

### New Method Data

- **Detection Times**:
  ```python
  [4, 3, 2, 1, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 4.5, 4.0, 3.6, 3.2, 2.8, 2.4, 2.0, 1.6, 1.2, 0.8]
  ```

- **Accuracies**:
  ```python
  [91, 93, 94, 96, 97, 98, 98.5, 99, 99.2, 99.5, 89, 91, 93, 95, 96, 97, 98, 98.5, 99, 99.5]
  ```

- **Coverage Efficiencies**:
  ```python
  [82, 87, 92, 97, 98, 98.5, 99, 99.2, 99.5, 99.8, 78, 82, 86, 90, 92, 94, 96, 97, 98, 99]
  ```

- **Response Times**:
  ```python
  [2.5, 2, 1.5, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 3.0, 2.6, 2.2, 1.8, 1.4, 1.0, 0.8, 0.6, 0.4, 0.2]
  ```

- **Scalability Data**:
  - **Number of UAVs**:
    ```python
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    ```
  - **Average Detection Times**:
    ```python
    [4, 3, 2, 1, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 4.5, 4.0, 3.6, 3.2, 2.8, 2.4, 2.0, 1.6, 1.2, 0.8]
    ```
  - **Average Response Times**:
    ```python
    [2.5, 2, 1.5, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 3.0, 2.6, 2.2, 1.8, 1.4, 1.0, 0.8, 0.6, 0.4, 0.2]
    ```

## Usage

### Prerequisites

- Python 3.x
- `matplotlib` and `numpy` libraries

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages**:
   ```bash
   pip install matplotlib numpy
   ```

### Running the Comparison Analysis

1. **Run the script**:
   ```bash
   python comparison_analysis.py
   ```

2. **View the results**: The script will generate plots comparing the existing method and the new method for each metric. The plots will be displayed in a window.

## Explanation of the Script

The script `comparison_analysis.py` performs the following steps:

1. **Imports necessary libraries**:
   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   ```

2. **Defines the `plot_comparison` function**: This function takes two dictionaries (`existing_data` and `new_data`) as inputs and generates plots for each metric.

3. **Example data for existing and new methods**: The script includes example data for both the existing and new methods.

4. **Calls the `plot_comparison` function**: The function is called with the example data to generate the comparison plots.

## Results

The script generates the following plots:

1. **Detection Time Over Simulation Steps**: Compares the detection times of the existing and new methods.
2. **Accuracy Over Simulation Steps**: Compares the accuracies of the existing and new methods.
3. **Coverage Efficiency Over Simulation Steps**: Compares the coverage efficiencies of the existing and new methods.
4. **Response Time Over Simulation Steps**: Compares the response times of the existing and new methods.
5. **Scalability - Detection Time**: Compares the average detection times of the existing and new methods as the number of UAVs increases.
6. **Scalability - Response Time**: Compares the average response times of the existing and new methods as the number of UAVs increases.

