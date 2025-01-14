'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

user_input = 'without,hello,bag,world'
parsed_words = user_input.split(',')
parsed_words.sort(key=lambda name: name.lower())

print(parsed_words)