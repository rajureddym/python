


new_list = []

if __name__ == '__main__':
    N = int(input())
    operations = {}
    for _ in range(N):
        op,*line = input.split()
        item = list(map(int,line))
        operations[op] = item

    for item in N:
        operation = input()
            if operation == 'print':
                funPrint()
            elif operation == 'insert':
                funInsert()
            elif operation == 'append':
                funAppend()
            elif operation == 'pop':
                funPop()
            elif operation == 'reverse':
                funReverse()
            else operation == 'sort':
                funSort()
            
            
 
            