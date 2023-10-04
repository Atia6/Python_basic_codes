# Python program for Sum of cubes of first n natural numbers

a = int(input('Insert a number:'))
ssum = 0
for i in range(1,a+1):
     ssum = ssum+i**3
print(f'Sum of cube of first {a} natural numbers is: {ssum}') 