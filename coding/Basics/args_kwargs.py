#return 5% of sum of given input values
def total(*args):
    print('\ngiven arguments to the function are: {}'.format(args))
    return (sum(args)) * 0.05

def myfunc(**kwargs):
    print('\ngiven key word arguments to the function are: {}'.format(kwargs))
    if 'fruit' in kwargs:
        print('Your fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
def combine_arg_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like to have {} {} now'.format(args[0],kwargs['fruit']))

if __name__ == "__main__":
    sum_value = total(10,100,200,0.1)
    print('5% of given argument sum is {}'.format(sum_value))
    myfunc(fruit='apple', veggie='lettuce')
    combine_arg_kwargs(10,20,30,40,fruit='apple', veggie='lettuce', food='noodles')