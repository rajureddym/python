
**comparison operators:**
>==,!= , <, >, <=, >=

**logical operators:**
>and, or, not

**statements:**

***If Elif and Else statements:***

* `control flow:` we only want to execute block of code when condition is met
* control flow syntax makes use of colons and indentation (whitespace)
* keywords:
    > if, elif, else

syntax examples:

>
    if some_condition:
        # block of code
    ---
    if some_condition:
        # execute some code
    else:
        # do something else
    --
    if some_condition:
        # execute some code
    elif some_other_condition:
        # do execute some other code
    else:
        # do something else   
    ---

***For loops examples:***

* many objects in python are `iterable` meaning every we can iterate over every element in a given object, for example every element in a list or every character in a string

example syntax:
>   
    variable = list/string/tuple/dict
    for <placeHolder/tempVariable> in iterableObjectName:
        # execute block of code

* tuple unpacking
>
    mylist = [(1,2),(3,4),(5,6),(7,8)]
    # return tuples
    for num in mylist:
        print(num)
    # returns each item in tuples
    for a,b in mylist:
        print(a)
        print(b)

* by default dict returns only keys
>
    d = {'k1':1,'k2':2,'k3':3}
    
    # returns keys k1,k2,k3
    for item in d:
        print(item)
    
    # to return entire item in tuple format (k1,1)
    for item in d.items():
        print(item)
    
    # to return only values of keys
    for key,value in d.items():
        print(value)

    for value in d.values():
        print(value)

***While loops:***

* syntax:
>
    while some_condition:
        # execute some code
    
    # we can combine while loop with else condition
    while some_condition:
        # execute some code
    else:
        # do something else

**useful keywords in loops:**

> break, continue, pass

* `break`: breaks out of the current closest enclosing loop
* `continue`: Goes to the top of the closest enclosing loop
* `pass`: does nothing at all
 
**Useful operators:**

* range(start, stop, step) -> generates numbers starts with 0 by default & in steps of 1 till specified number
>
    for n in range(10)
    print(n) // 0 to 9

    for n in range(0,10,2)
    print(n) // 0,2,4,6,8

    #casting
    list(range(0,11,2)) -> [0,2,4,6,8,10]

* enumerate:
>
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

    --> 
    (0, 'a')
    (1, 'b')
    (2, 'c')
    (3, 'd')

    #tuple unpacking
    print('\nlets use enumerare function & unpack tuple returned by enumerate\n')
    for index, char in enumerate(word):
        print('the letter {} is at {}'.format(char, index))

* zip: joins/zips iterable object items with their respective indexes, returns an tuple object. Zip takes lowest length object & zip only those number of items in given objects

> 
    mylist1 = ['a','b','c']
    mylist2 = [1,2,3,4]
    mylist3 = ['w','x','y','z']


    #zip returns a list of tuple items
    print(zip(mylist1,mylist2,mylist3)) 

    --> 
    [('a', 1, 'w'), ('b', 2, 'x'), ('c', 3, 'y')]

    #print each item in tuple format after zipping
    for item in zip(mylist1,mylist2,mylist3):
        print item

    -->      
    ('a', 1, 'w')
    ('b', 2, 'x')
    ('c', 3, 'y')

* `in`:  to check item in iterable object, returns True/False
* `min & max`: returns min & max of given object
* `random`: random library has couple of imprt builtin function such as shuffle(), randint(start, end) etc
* `input`: to accept user input, always accepts input as string