def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
        
result1= lesser_of_two_evens(2,4)
print(result1)
result2=lesser_of_two_evens(10,9)
print(result2)


def animal_crackers(text):
    a = text.split(" ")
    first_word = a[0]
    second_word = a[1]
    if list(first_word)[0] == list(second_word)[0]:
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
