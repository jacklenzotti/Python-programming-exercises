'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
'''

user_input = '3,5' 

[rowNum, colNum] = user_input.split(',')

multilist = [[0 for col in range(int(colNum))] for row in range(int(rowNum))]

for row in range(int(rowNum)):
    for col in range(int(colNum)):
        multilist[row][col]= row*col

print(multilist)