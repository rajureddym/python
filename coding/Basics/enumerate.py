#!/bin/python3

index_count =  0
word = 'abcd'

print('\nlets print char\'s in a string using traiditional method\n')
for letter in word:
    print(('the letter {} is at location {} in word {}').format(letter,index_count,word))
    index_count +=1 

#enumerate returns tuple with index & item
print('\nlets use enumerare function without having to use counter\n')
for letter in enumerate(word):
    print(letter)

#tuple unpacking
print('\nlets use enumerare function & unpack tuple returned by enumerate\n')
for index, char in enumerate(word):
    print('the letter {} is at {}'.format(char, index))