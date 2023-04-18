#print n elements of fibnacci sequence using loop where n is positve integer
n = 6
fib_seq=[]
first = 0
second = 1
i=1
fib_seq=[0,1]
while len(fib_seq)<=n:
    third=first+second
    fib_seq.append(third)
    first=second
    second=third
    i=i+1

print(fib_seq)