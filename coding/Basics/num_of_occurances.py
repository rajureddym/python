a='RajuPinkyMyaka'
char_list=[]

for char in a:
    char_list.append(char)
print(char_list)
set_char_list=set(char_list)
print(set_char_list)

for i in range(len(set_char_list)):
    print(a[i] + ' is repeated ' + str(a.count(a[i])))