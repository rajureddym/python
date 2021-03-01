#!/bin/python3

a = " Hello World! "

print("\nlength before removing whitespaces: " + str(len(a)))
a = a.strip()
print("\nstring after removing whitespaces: "+ a)
print("\nlength before removing whitespaces: " + str(len(a)))


print("\nconvert string to uppper case letters: " + a.upper())

print("\nconvert string to lower case letters: " + a.lower())

print("\ncapitalizing string: " + a.capitalize())
#split by whitespace by default
print("\nsplit string with whitespace: ")
print(a.split(" ")) 

#we can mention split char or anything
print("\nsplit string with a char: ")
print(a.split('l')) 

#returns first index during left to right scan
print("\nfirst index of a given substring in string from left to right: " + str(a.find('llo')))

#return index from right to left scan
print(a.rfind('llo'))

print("\nreplacing given substring with given string: " + a.replace("World", "Nagaraju"))

