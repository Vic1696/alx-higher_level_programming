#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    #Check if matrix = None. 
    #If None, assign an empty list
    if matrix is None:
        matrix = []
    
    # Use a list comprehension for clarity and conciseness
    new_matrix = [[x**2 for x in row] for row in matrix]
    
    return new_matrix
