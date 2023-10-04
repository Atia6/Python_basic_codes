# python program for factorial of a number

a = int(input('Insert a number:'))
fact = 1
for i in range(1,a+1):
    
    fact = fact * i

    
print(f'The factorial of {a} is {fact}')