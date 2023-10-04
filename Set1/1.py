#1. Write a program that does the following in order:
#• Asks the user to enter a number “x”
#• Asks the user to enter a number “y” 
#• Prints out number “x”, raised to the power “y”.
#• Prints out the log (base 2) of “x”.

x = int(input("Enter a number :"))
y = int(input("Enter a number :"))

print("Output 1:",x**y)

import math

print('Output 2:',math.log2(x))