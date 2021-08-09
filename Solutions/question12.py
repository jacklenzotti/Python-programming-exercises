'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

solution = []

for x in range(1000, 3001):
    y = str(x)
    if int(y[0]) % 2 == 0 and int(y[1]) % 2 == 0 and int(y[2]) % 2 == 0 and int(y[3]) % 2 == 0:
        solution.append(y)

print(','.join(solution))