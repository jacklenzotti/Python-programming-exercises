'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

solution = []

def compute_factorial(x):
    if x == 0:
        return 1
    return x * compute_factorial(x - 1)

for index in range(0, len(sys.argv)):
    if index == 0:
        continue
    computed_value = compute_factorial(int(sys.argv[index]))
    solution.append(str(computed_value))

print(','.join(solution))