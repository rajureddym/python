from random import shuffle

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Please enter the guess 0,1 or 2: ')
    return int(guess)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Congratulations! Your guess is correct:')
        print(mylist)
    else:
        print('Sorry, Wrong guess. Try again to test your luck!')
        print(mylist)

if __name__ == '__main__':
    # read input guess from customer
    mylist = [' ', 'O', ' ']
    guess = player_guess()
    #print(guess)
    mixed_list = shuffle_list(mylist)
    #print(mixed_list)
    check_guess(mixed_list, guess)
