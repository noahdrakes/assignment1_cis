# MODULE THAT CONTAINS ALL OF THE FRAME TRANSFORMATION ALGORITHMS

import numpy as np

# created function to combine rotation matrix with position vector 
# to get 4x4 fram transformation matrix

def create_frame_transformation_matrix(rotation_matrix, position_vector):
    frame_transformation_matrix = np.empty((4, 4), dtype=object)
    rows, columns = rotation_matrix.shape

    # check if rotation matrix is the right size (3x3)
    if (rows != 3 & columns != 3):
        print("Rotation matrix is wrong size!")
    
    # fill the transformation matrix with rotation elements
    for i in range(0, 3):
        for j in range(0,3):
            frame_transformation_matrix[i][j] = rotation_matrix[i][j]
    
    ## load position vector into frame transformation matrix
    frame_transformation_matrix[0][3] = position_vector[0] #set the x of position vector
    frame_transformation_matrix[1][3] = position_vector[1] #set the y of position vector
    frame_transformation_matrix[2][3] = position_vector[2] #set the z of position vector

    frame_transformation_matrix[3][3] = 1
    frame_transformation_matrix[3][0] = 0
    frame_transformation_matrix[3][1] = 0
    frame_transformation_matrix[3][2] = 0

    return frame_transformation_matrix


# function to perform frame transformation on a point vector
# parameters:   frame_transformation matrix -> 4x4 matrix
#               position vector: vector that the frame transformation will occur on 
# return        new transposed vector position 
 
def transform_vector(frame_transformation_matrix, position_vector):

    rows, columns = frame_transformation_matrix.shape

    if (rows != 4 & columns != 4):
        print("frame transformation matrix is not 4 x 4!")
        return None

    position_vector.transpose()

    return frame_transformation_matrix.dot(position_vector)

    
# Algorithim 3D point set to 3D point set registration algorithm

# using the quaternion method 
# REFERENCE: SLIDE 25: https://ciis.lcsr.jhu.edu/lib/exe/fetch.php?media=courses:455-655:lectures:rigid3d3dcalculations.pdf

# parameters 
# matA is a matrix that contains the initial x y z positions 
# 
# Eg: matA[0][0] = x0 , matA[0][1] = y0, matA[1][0] x1, matA[1][2] = z2 and so on 
#
# matB is a matrix that contains the transposed coordinates 

def calculate_point_cloud_registration(matA, matB):

    # STEP 1: CALCULATE H

    H = np.zeros((3,3), dtype=object)
    new_Matrix = np.zeros((3,3), dtype=object)

    rows, columns = matA.shape
    for k in range(0, rows):
        for i in range(0, 3):
            for j in range(0,3):
                new_Matrix[i][j] = matA[k][i] * matB[k][j]
        H += new_Matrix

    
    # STEP 2: CALCULATE G
    G = np.zeros((4,4), dtype=object)

    traceH = H.trace()
    print(traceH)

    deltaT = np.array([H[1][2]-H[2,1] , H[2][0] - H[0][2] , H[0][1] - H[1][0] ])
    delta = deltaT.transpose()

    print("deltaT:")
    print(delta.transpose())

    print("test array:")
    x = np.array([1, 2 , 3])
    print(x)

    print(x.transpose())

    


def calculate_point_cloud_registration_svd(matA, matB):

    # STEP 1: CALCULATE H

    H = np.zeros((3,3), dtype="float64")
    new_Matrix = np.zeros((3,3), dtype="float64")

    rows, columns = matA.shape
    for k in range(0, rows):
        for i in range(0, 3):
            for j in range(0,3):
                new_Matrix[i][j] = matA[k][i] * matB[k][j]
        H += new_Matrix

    
    # STEP 2: COMPUTE SVD
    U, S, VT = np.linalg.svd(H)

    # STEP 3: COMPUTE R
    R = np.dot(VT.T,  U.T)

    # STEP 4: Validate Determinant
    determinant = np.linalg.det(R)

    if determinant <= 1.000001 and determinant > 0.9999:
        return R
    else:
        return None

    


    
    

    

