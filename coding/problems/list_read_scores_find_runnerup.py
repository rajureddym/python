if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(set(list(arr)))
    print('printing list of scores after removing duplicates: ' + str(a))
    print('printing list of scores after removing duplicates & sorting : ')
    a.sort()
    print(a)
    print('runner up score in a given list is: ' + str(a[-2]))