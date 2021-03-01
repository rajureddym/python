import textwrap

def wrap(string, max_width):
    a = textwrap.fill(string,max_width)
    return a

"""    
#return in list format
    a = textwrap.wrap(string,max_width)
    for item in a:
        print(item)
#using traditional loop approach
    i = 0
    while(i<=(len(string)-max_width)):
        print(string[i:i+max_width])
        i = i + max_width
    print(string[i:])
"""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)