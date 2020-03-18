""" Solves q18 from 2015 Advent of code """
import numpy as np

def read_f(f):
    matrix = np.zeros((102, 102), dtype=int)
    string_matrix = []
    for line in f:
        string_matrix.append(line)
    for i in range(100):
        for j in range(100):
            if string_matrix[i][j] == '#':
                matrix[i+1][j+1] = 1
    return matrix

def animate(matrix):
    animated_matrix = np.zeros((102, 102), dtype=int)
    for i in range(1, 101):
        for j in range(1, 101):
            on_lights = 0
            on_lights += matrix[i][j-1]
            on_lights += matrix[i+1][j-1]
            on_lights += matrix[i+1][j]
            on_lights += matrix[i+1][j+1]
            on_lights += matrix[i][j+1]
            on_lights += matrix[i-1][j+1]
            on_lights += matrix[i-1][j]
            on_lights += matrix[i-1][j-1]
            if matrix[i][j] == 1:
                if on_lights in (2,3):
                    animated_matrix[i][j] = 1
                else:
                    animated_matrix[i][j] = 0
            elif on_lights == 3:
                animated_matrix[i][j] = 1
    return animated_matrix

def main():
    with open('inputQ18.txt', 'r') as f:
        matrix = read_f(f)
        for i in range(100):
            matrix = animate(matrix)
        i = np.count_nonzero(matrix)
        print(i)

if __name__ == '__main__':
    main()
