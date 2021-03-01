#!/bin/python3

mylist1 = ['a','b','c']
mylist2 = [1,2,3,4]
mylist3 = ['w','x','y','z']


#zip returns a list of tuple items
print(zip(mylist1,mylist2,mylist3))

#print each item in tuple format after zipping
for item in zip(mylist1,mylist2,mylist3):
    print item

