import numpy as np 

matrix = np.array([
    [1,3,5],
    [4,2,8],
    [6,3,7]
    ])

# determinal
det_col1 = (matrix[0][0] * (((matrix[2][2]) * (matrix[1][1])) - ((matrix[1][2]) * (matrix[2][1]))))
det_col2 = (matrix[0][1] * (((matrix[1][0]) * (matrix[2][2])) - ((matrix[1][2]) * (matrix[2][0]))))
det_col3 = (matrix[0][2] * (((matrix[1][0]) * (matrix[2][1])) - ((matrix[1][1]) * (matrix[2][0]))))
det = det_col1 - det_col2 + det_col3

print(f"DET: {det}")


#invers
if det == 0:
    print("ERR!")
else:
    cofactors = np.array([
        [ (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]),
          -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
          (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) ],

        [-(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]),
          (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]),
          -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]) ],

        [ (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]),
          -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]),
          (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) ]
    ])

    adjugate = cofactors.T

    inv_matrix = adjugate / det
    print(inv_matrix)