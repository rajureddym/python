***Python Objects & Data Structures:***

**Variable:**
   * Naming 
        can't start with number, 
        can't have space (use _)
        can't use special characters 
   * recommended to use lower case (Global variable written in CAPs)
   * Dynamic Typing:
     >   
            my_dogs = 2,
            my_dog = ["foo","bar"]

        * in other languages variables are static types i.e. we define variable with data type up front,
            >
                int my_dogs = 2
                my_dogs = "puppy" //results in error

        * pro - fast development & easy to work, readability 
        * cons - may result in bug for unexpected data type, we need to use built-in fun type()

**Strings:**

- sequence of characters defined in single or double quotes 
- because of ordered sequencing we can use *indexing* & *slicing* to grab sub-section of string 

* Indexing:
>
    char:        h    e   l   l    o 
    index:       0    1   2   3    4
    re-index:   -5   -4   -3  -2  -1 

* Slicing:  **[start:stop:step]**
    - stop -> go up to but not include that 
> 
    a[:] -> hello
    a[:4] -> hell
    a[1:] -> ello
    a[::2] -> hlo
    a[::-1] -> (reserves string) -> olleh

*string properties & methods:*
 
* String concatenation:
        - strings are immutable i.e can't use indexing to replace individual element/item/char in a string, we need to use concatenation
    >
            a = "Hello World!",
            a = a + " Welcome",
            a -> "Hello world! Welcome"

* String multiplication:
     >
        a = z
        a * 10 -> zzzzzzzzzz

* general 
>
     a.upper() 
     a.lower()
     a.split() -> split by whitespace by default, or we can mention
        ['Hello', 'World']
     a.split(l) -> ['He','o Wor', 'd']
    
* String interpolation:
     >
        my_name = "Raju"
        print("Hello " + my_name)
            Hello Raju

    * .format() method:
    >
        print('My name is {}'.format('Raju'))
            My name is Raju
        
        print('The {} {} {}'.format('fox','brown','quick'))
            The fox brown quick
        
        print('The {2} {1} {0}'.format('fox','brown','quick'))  
            The quick brown fox
        
        print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
            The quick brown fox
    * float formatting method -> {value.width.precision f}
    >
        example:
        result = 100/777
        result -> 0.128700122
        print("The result was {}".format(result)) -> The result was 0.128700122
        print("The result was {r}".format(r=result)) -> The result was 0.128700122
        print("The result was {r.1.3f}".format(r=result)) -> The result was 0.129
        print("The result was {r.5.3f}".format(r=result)) -> The result was      0.129

    * formatted string literals (released in 3.6)
    >
        name = Raju
        age = 25
        print('My name is {}'.format('name'))
            My name is Raju 
        print(f'My name is {name}')
            My name is Raju  
        print(f'{name} is {age} years old')   
            Raju is 25 years old    

**List:**
* list is a ordered sequence that can hold variety of objects, included in []
* supports indexing & slicing
* supports concatenation 
* list is mutable i.e. we can replace an object in a given list (string doesn't supports)
>
        num_list = ["one", "two", "three", "four"]
        num_list[0] = 'ONE IN ALL CAPS'
        num_list -> ["ONE IN ALL CAPS", "two", "three", "four"]
* methods 
    * .append() -> at end of list
    * .pop() -> removes item/object at end of list, can remove any item with index
    * .sort() -> does in-place sort, doesn't return any value
    * .reverse() -> does in-place reverse, doesn't return any value

**Dictionaries:**
* unordered mappings to store objects in format of key-value store
* value can be string, another list or another key/value pair
* can override a value of key and can append new object to dict
>
    d = {'k1':100, 'k2': 200}
    d[k3]=300
    
    d -> {'k1':100, 'k2': 200, 'k3':300}
    d[k1] = 400
    
    d -> {'k1':400, 'k2': 200, 'k3':300}
    
    d.keys() -> dict_keys(['k1','k2','k3'])
    
    d.values() -> dict_values([400,200,300])
    
    d.items() -> dict_items([(k1,400),(k2,200),(k3,300)])

*List vs Dictionaries:*
* objects are retrieved by location Vs objects are retrieved by 'key' name vs 
* as it's ordered sequence it can be indexed/sliced/sorted Vs as it's unordered, it can't be sorted 

**Tuples:**
* similar to list but can't be reassigned or doesn't allow item assignment i.e. immutable 
* uses parenthesis (1,2,3)
* slicing, indexing allowed
* .count() -> returns number of times item repeated in tuple
* .index() -> returns index position of item
* Tuples are used when compared to list is -> to protect data being accidentally changed when passing around in prog,data integrity  

**Sets:**
* set are unordered collection of unique items
>
    myset = set()
    myset.add(1)
    myset.add(2)
    myset -> {1,2}
    myset.add(2) <-- only unique items allowed, so output will be same
    myset -> {1,2}

* casting list/string
> 
    mylist = [1,1,1,3,3,3,2,2,2]
    set(mylist)  <- returns unique values in list
        {1,3,2}
    set('Mississippi')
        {'M','i','s','p'}

**Booleans:**
* operators that allow us to convey True or False statement

**I/O with basic files:**

    myfile = open('') -> open a file
    myfile.read() -> output the contents
    myfile.readlines() -> output each line of a file into element/object in a list
    myfile.seek() -> to move cursor position to the start of file
    myfile.close() -> to close the opened file 

> Instead of opening & taking care of closing we can do this way so we don't required bother about closing
 
    with open('myfile.txt') as my_new_file:
        contents = my_new_file.read()

    with open('myfile.txt', mode='r') as my_new_file:
        contents = my_new_file.read()

file modes:
>
    r -> read only
    w -> override exiting file or write to new file if file doesn't exits.
    a -> append at end of file
    r+ -> reading n writing 
    w+ -> writing and reading





