#Maximum of two numbers

a = int(input('Insert 1st number:'))
b = int(input('Insert 2nd number:'))

if a>b:
    print(f'Maximum of the given two numbers is {a}')
elif a<b:
    print(f'Maximum of the given two numbers is {b}')
else:
    print(f'The numbers are equal.')