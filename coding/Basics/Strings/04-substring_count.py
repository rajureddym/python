def count_substring(string, sub_string):
    count = 0 
    sublen = len(sub_string)
    for i in range(len(string)):
        if(string[i:i+sublen] == sub_string):
            count += 1
    return count

if __name__ == '__main__':
    print("\nEnter the string: ")
    string = input().strip()
    print("\nEnter the substring: ")
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(f"\nThe substring `{sub_string}` is repeated {count} times in a given string `{string}`")