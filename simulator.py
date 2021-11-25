import numpy as np
import globals as gb
import random as rand

'''
A Space Simulator ?
description here
@author Francisco Reyna

University of Texas at Austin
College of Natural Sciences, Computer Science
'''


# Main
def main ():
    global arr
    arr = [ [0]*gb.SIM_SIZE for i in range(gb.SIM_SIZE)]
    arr = fill_matrix (arr, gb.SIM_SIZE)
    print_matrix (arr, gb.SIM_SIZE)

# Fills the matrix with data
def fill_matrix (matrix, side_len):
    choices = [gb.PLANET_STR, gb.STAR_STR, gb.BLACK_HOLE_STR, gb.NOTHING_STR]
    weights = [0.14, 0.04, 0.02, 0.8]

    for i in range (int(side_len)):
        for j in range (int(side_len)):
            slot_type = (str(np.random.choice(choices, 1, p=weights)[0])).strip()

            if (slot_type == gb.STAR_STR):
                matrix[i][j] = '*'
            elif (slot_type == gb.PLANET_STR):
                matrix[i][j] = 'x'
            elif (slot_type == gb.BLACK_HOLE_STR):
                matrix[i][j] = 'O'
            elif (slot_type == gb.NOTHING_STR):
                matrix[i][j] = '.'

            
    return matrix

# Debugging function for the global array
def print_matrix (matrix, side_len):
    for i in range (int(side_len)):
        print ('[ ' + str(matrix[i][0]), end='')
        for j in range (1, int(side_len)):
            print (', ' + str (matrix[i][j]), end='')
        print (']') # new line for new row      

# Script driver function
if __name__ == '__main__':
    main()