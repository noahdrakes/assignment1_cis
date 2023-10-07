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

    


def calculate_rotation_transformation(matA, matB):
    # STEP 1: CALCULATE STD DEVIATION OF mat A and B and the sigma

    a_tilda = calculate_stddeviation(matA)
    b_tilda = calculate_stddeviation(matB)
    sigma = calculate_sigma(matA, matB)

    # STEP 2: CALCULATE H

    H = np.zeros((3,3))
    new_Matrix = np.zeros((3,3))

    rows, columns = a_tilda.shape
    # for k in range(0, rows):
    #     for i in range(0, 3):
    #         for j in range(0,3):
    #             new_Matrix[i][j] = a_tilda[k][i] * b_tilda[k][j]
    #     H += new_Matrix

    for _a, _b in list(zip(a_tilda, b_tilda)): 
        H_temp = np.array([[_a[0]*_b[0], _a[0]*_b[1], _a[0]*_b[2]], 
                            [_a[1]*_b[0], _a[1]*_b[1], _a[1]*_b[2]], 
                            [_a[2]*_b[0], _a[2]*_b[1], _a[2]*_b[2]]])

  
    H = H_temp
    # STEP 3: COMPUTE SVD
    U, S, VT = np.linalg.svd(H)

    # STEP 4: COMPUTE R
    R = np.dot(VT.T,  U.T)

    # if np.linalg.det(R) < 0:
    #     VT[-1,:] *= -1

    # STEP 5: Validate Determinant
    determinant = np.linalg.det(R)

    # if determinant <= 1.000001 and determinant > 0.9999:
    #     return R
    # else: 
    #     return None

    return R



def calculate_translation_transformation(matA, matB, R):
    a_bar = calculate_mean(matA)
    b_bar = calculate_mean(matB)
    return b_bar - np.dot(R, a_bar)




def calculate_point_cloud_registration_svd(matA, matB):
    R = calculate_rotation_transformation(matA, matB)
    p = calculate_translation_transformation(matA, matB, R)
    return R, p



    



#### MATH METHODS #####

def calculate_mean(matrix):
    return np.mean(matrix,axis = 0)

def calculate_stddeviation(matrix):
    return matrix - calculate_mean(matrix)

def calculate_sigma(matA, matB):
    a_tilda = calculate_stddeviation(matA)
    b_tilda = calculate_stddeviation(matB)

    return (np.linalg.norm(b_tilda, axis=0))/(np.linalg.norm(a_tilda, axis=0))