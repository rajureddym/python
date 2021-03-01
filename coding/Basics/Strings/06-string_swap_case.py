def swap_case(s):
    a = list(s)
    index = 0
    for i in a:
        l = a[index]
        if l.isupper():
            a[index] = i.lower()
        else: 
            a[index] = i.upper()
        index +=1
    b = "".join(a)
    return b
    

if __name__ == '__main__':
    print("\nEnter the String to swap each character\'s case: ")
    s = input()
    result = swap_case(s)
    print("\nString after swapping each char case: " + result)