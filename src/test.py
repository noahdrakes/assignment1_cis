import numpy as np
from math import radians

# Define the 3D points matrix
points_matrix = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
    [10.0, 11.0, 12.0],
    [13.0, 14.0, 15.0],
    [16.0, 17.0, 18.0],
    [19.0, 20.0, 21.0],
    [22.0, 23.0, 24.0],
    [25.0, 26.0, 27.0],
    [28.0, 29.0, 30.0]
])

# Define rotation angles in degrees
angle_x = radians(30)
angle_y = radians(40)
angle_z = radians(60)

# Define translation vector
translation = np.array([12.0, 3.0, 4.0])

# Rotation matrices for x, y, and z axes
rotation_x = np.array([
    [1, 0, 0],
    [0, np.cos(angle_x), -np.sin(angle_x)],
    [0, np.sin(angle_x), np.cos(angle_x)]
])

rotation_y = np.array([
    [np.cos(angle_y), 0, np.sin(angle_y)],
    [0, 1, 0],
    [-np.sin(angle_y), 0, np.cos(angle_y)]
])

rotation_z = np.array([
    [np.cos(angle_z), -np.sin(angle_z), 0],
    [np.sin(angle_z), np.cos(angle_z), 0],
    [0, 0, 1]
])

# Apply rotation and translation to the points
rotated_points = np.dot(np.dot(np.dot(points_matrix, rotation_x), rotation_y), rotation_z) + translation

# Print the transformed points
print("Transformed 3D Points:")
print(rotated_points)
