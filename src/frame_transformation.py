import numpy as np

def create_frame_transformation_matrix(rotation_matrix, position_vector):
    frame_transformation_matrix = np.empty((4, 4), dtype=object)
    rows, columns = rotation_matrix.shape

    if (rows != 3 & columns != 3):
        print("Rotation matrix is wrong size!")
    
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


def transform_vector(frame_transformation_matrix, position_vector):

    rows, columns = frame_transformation_matrix.shape

    if (rows != 4 & columns != 4):
        print("frame transformation matrix is not 4 x 4!")
        return None

    position_vector.transpose()

    return frame_transformation_matrix.dot(position_vector)

    



