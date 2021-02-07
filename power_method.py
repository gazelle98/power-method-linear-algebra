import sys
import numpy as np


def get_input():
    # Reading order of matrix
    n = int(input('Enter order of matrix: '))

    # Making Numpy array of n x n size and initializing
    # to zero for storing matrix
    a = np.zeros((n, n))

    # Reading matrix
    print('Enter Matrix Coefficients:')
    for i in range(n):
        for j in range(n):
            a[i][j] = float(input(f'a[{i}][{j}] = '))

    # Making Numpy array n x 1 size and initializing to zero
    # for storing initial guess vector
    eigen_vector = np.zeros((n))

    # Reading initial guess vector
    print('Enter initial guess vector: ')
    for i in range(n):
        eigen_vector[i] = float(input(f'x[{i}] = '))

    # Reading tolerable error
    tolerable_error = float(input('Enter tolerable error: '))

    # Reading maximum number of steps
    max_iteration = int(input('Enter maximum number of steps: '))

    return(a, eigen_vector, tolerable_error, max_iteration)


def print_result(step, eigen_value, eigen_vector):
    print(f'\nSTEP {step}')
    print('-------------')
    print('Eigen Value = ' + str(eigen_value))
    print('Eigen Vector = [', end='')
    print(*eigen_vector, end='')
    print(']')


def solve(a, eigen_vector=None, max_iteration=10, tolerable_error=0.001):
    step = 1
    condition = True
    lambda_old = 1.0

    if eigen_vector is None:
        eigen_vector = [1] * len(a)

    # Power Method Implementation
    while condition:
        # Multiplying a and x
        eigen_vector = np.matmul(a, eigen_vector)

        # Finding new Eigen value and Eigen vector
        lambda_new = max(abs(eigen_vector))

        eigen_vector = eigen_vector / lambda_new
        print_result(step, lambda_new, eigen_vector)

        # Checking maximum iteration
        step += 1
        if step > max_iteration:
            print('Not convergent in given maximum iteration!')
            break

        # Calculating error
        error = abs(lambda_new - lambda_old)
        print(f'error = {error}')
        lambda_old = lambda_new
        condition = error > tolerable_error


if __name__ == '__main__':
    for i, arg in enumerate(sys.argv):
        # import pdb; pdb.set_trace()
        if arg == '--m' or arg == 'matrix':
            if sys.argv[i + 1] == 'input':
                # Getting variables from input and terminal
                a, eigen_vector, tolerable_error, max_iteration = get_input()
                solve(a, eigen_vector, max_iteration, tolerable_error)

            elif sys.argv[i + 1] == 'default':
                # An easy and simple matrix for default mode
                a = [[5, 4], [1, 2]]
                eigen_vector = [1] * len(a)
                tolerable_error = 0.001
                max_iteration = 10
                solve(a, eigen_vector, max_iteration, tolerable_error)

            elif sys.argv[i + 1] == 'input_file':
                # Getting variables from an input file with
                # the wanted structure
                a = []
                with open('input.txt', 'r') as file:
                    lines = file.readlines()
                    max_iteration = int(lines[-1].strip().split()[0])
                    tolerable_error = float(lines[-2].strip().split()[0])
                    eigen_vector = [int(i) for i in lines[-3].strip().split()]
                    for i in range(0, len(lines) - 3):
                        a.append([int(i) for i in lines[i].strip().split()])
                    solve(a, eigen_vector, max_iteration, tolerable_error)

            else:
                ValueError('Given argument is not valid.')
