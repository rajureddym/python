if __name__ == '__main__':
    print('Enter the value of x: ')
    x = int(input())
    print('Enter the value of y: ')
    y = int(input())
    print('Enter the value of z: ')
    z = int(input())
    print('Enter the value of sum: ')
    n = int(input())

b = []

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0, z+1):
            if i+j+k !=n:
                a = [i,j,k]
                b.append(a)

print(b)