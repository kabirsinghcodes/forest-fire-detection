# computer_vision.py
import cv2
import numpy as np

def detect_fire(image):
    # Convert image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Define range for fire color
    lower_fire = np.array([18, 50, 50])
    upper_fire = np.array([35, 255, 255])
    # Threshold the HSV image to get only fire colors
    mask = cv2.inRange(hsv, lower_fire, upper_fire)
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# Example usage
image = cv2.imread('forest_fire.jpg')
contours = detect_fire(image)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow('Fire Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()