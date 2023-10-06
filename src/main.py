import numpy as np
from transforms3d import euler as e
import frame_transformation as fp
# from transforms3d.derivations import eulerangles

### 1. Develop (or develop proficiency with) a Cartesian math package for 3D points, rotations, and frame transformations ###

# converting rotation for each xyz axis to be in radians (60, 30, 30 degrees respectively)
x_rotation = np.deg2rad(60)
y_rotation = np.deg2rad(30)
z_rotation = np.deg2rad(30)

# converting angles into rotation matrices
rotation_matrix = e.euler2mat( z_rotation ,x_rotation, y_rotation, 'szxy')
print("rotation matrix:")
print(rotation_matrix)

#creating position vector
pos_vector = np.empty((3,0), dtype=object)
pos_vector = 10, -5, 4

# creating frame transformation matrix
ft_matrix = np.empty((4,4), dtype=object)
ft_matrix = fp.create_frame_transformation_matrix(rotation_matrix, pos_vector)
print("frame transformation matrix:")
print(ft_matrix)

# creating new vector for point transformation
transposed_pos_vector = np.array([6, -4, 1, 1])

# obtaining transposed point
transformed_vector = fp.transform_vector(ft_matrix, transposed_pos_vector)
print(transformed_vector)