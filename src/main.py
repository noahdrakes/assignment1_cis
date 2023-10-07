import numpy as np
from transforms3d import euler as e
from transforms3d import quaternions as q
import frame_transformation as ft
import random
# from transforms3d.derivations import eulerangles

### 1. Develop (or develop proficiency with) a Cartesian math package for 3D points, rotations, and frame transformations ###

# converting rotation for each xyz axis to be in radians (60, 30, 30 degrees respectively)
x_rotation = np.deg2rad(60)
y_rotation = np.deg2rad(30)
z_rotation = np.deg2rad(30)

# converting angles into rotation matrices
rotation_matrix = e.euler2mat( z_rotation ,x_rotation, y_rotation, 'szxy')
print("rotation matrix:")
# print(rotation_matrix)

# converting rotation matrix to quaternion
quaternion_matrix = q.mat2quat(rotation_matrix)
print("quaternion matrix")
# print(quaternion_matrix)

#creating position vector
pos_vector = np.empty((3,0), dtype=object)
pos_vector = 10, -5, 4

# creating frame transformation matrix
ft_matrix = np.empty((4,4), dtype=object)
ft_matrix = ft.create_frame_transformation_matrix(rotation_matrix, pos_vector)
print("frame transformation matrix:") 
# print(ft_matrix)

# creating new vector for point transformation
transposed_pos_vector = np.array([6, -4, 1, 1])

# obtaining transposed point
transformed_vector = ft.transform_vector(ft_matrix, transposed_pos_vector)
# print(transformed_vector)



###########################################################################

# 2. Develop a 3D point set to 3D point set registration algorithm

# using the quaternion method 
# REFERENCE: SLIDE 25: https://ciis.lcsr.jhu.edu/lib/exe/fetch.php?media=courses:455-655:lectures:rigid3d3dcalculations.pdf

# parameters 
# matA is a matrix that contains the initial x y z positions where matA[00], mat[0][1], mat[0][1] = x0 , y0, z0 respectively
# matB is a matrix that contains the transposed coordinates 





###########################################################################

#TEST HERE#
A, B = np.empty((3,3), dtype="float"), np.empty((3,3), dtype="float")
for i in range(0,3):
    for j in range(0,3):
        A[i][j] = random.uniform(1.5, 10.2)
        B[i][j] = random.uniform(1.5, 10.2)


# ft.calculate_point_cloud_registration(A, B)
ft.calculate_point_cloud_registration_svd(A,B)


print("MEAN: ")
print(ft.calculate_mean(A))

print("STD: ")
print(ft.calculate_stddeviation(A))

print("DETERMINANT")
print(np.linalg.det(ft.calculate_rotation_transformation(A,B)))



#TEST HERE#








# linear algebra methods

# svd and least squares solver
# - np.linalg.svd()
# - np.linalg.lstsq()




## TODO 
# - create data structure to hold frame data F = [R,p]
# - write algorithm for point to point set registration 