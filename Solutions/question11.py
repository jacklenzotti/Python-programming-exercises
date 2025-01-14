'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''

user_input = '0100,0011,1010,1001'

values = list(filter(lambda x: x % 5 == 0, [int(x, 2) for x in user_input.split(',')]))
print(','.join(list(map(lambda x: '{0:b}'.format(x), values))))