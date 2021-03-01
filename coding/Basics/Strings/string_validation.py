if __name__ == '__main__':
    print("\nEnter the String to validate: ")
    s = input()
print(f"\nThe given string `{s}` is alphanumeric: " + str(s.isalnum()))
print(f"\nThe given string\'s `{s}` chartecters are alphabetical: " + str(s.isalpha()))
print(f"\nThe given string `{s}` is numeric: " + str(s.isdigit()))
print(f"\nThe given string `{s}` is lowercase: " + str(s.islower()))
print(f"\nThe given string `{s}` is uppercase: " + str(s.isupper()))