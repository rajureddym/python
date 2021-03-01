def print_formatted(number):
    # your gode goes here
    for i in range(1,number+1):
        print("{a} {b} {c} {d}".format(a=i, b=oct(i),c=hex(i),d=bin(i)))
        i += 1

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)