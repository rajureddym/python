#Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    a = list(string)
    a[position] = str(character)
    word = "".join(a)
    return word

"""     a = string[:position] + str(character) + string[position+1:]
    return a """

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)