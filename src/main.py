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
A, B = np.empty((3,3)), np.empty((3,3))
for i in range(0,3):
    for j in range(0,3):
        A[i][j] = random.uniform(1.5, 10.2)
        B[i][j] = random.uniform(1.5, 10.2)


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

transformed_points = np.array([
[14.66844853,  4.84221318,  5.86698501],
 [19.01363841,  5.51227596 , 8.63652302],
 [23.35882829,  6.18233875, 11.40606103],
 [27.70401817,  6.85240153 ,14.17559904],
 [32.04920805 , 7.52246431, 16.94513705],
 [36.39439793,  8.1925271 , 19.71467506],
 [40.73958781,  8.86258988 ,22.48421306],
 [45.08477768,  9.53265267, 25.25375107],
 [49.42996756, 10.20271545, 28.02328908],
 [53.77515744, 10.87277824, 30.79282709]])

# ft.calculate_point_cloud_registration(A, B)
R, p = ft.calculate_point_cloud_registration_svd(points_matrix,transformed_points)





print("MEAN: ")
print(ft.calculate_mean(A))

print("STD: ")
print(ft.calculate_stddeviation(A))

print("DETERMINANT")
print(np.linalg.det(ft.calculate_rotation_transformation(A,B)))


R = e.mat2euler(R)
R = np.rad2deg(R)

print("R")
print(R)
print("P")
print(p)

#TEST HERE#








# linear algebra methods

# svd and least squares solver
# - np.linalg.svd()
# - np.linalg.lstsq()




## TODO 
# - create data structure to hold frame data F = [R,p]
# - write algorithm for point to point set registration 