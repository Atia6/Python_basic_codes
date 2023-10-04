#Given three Points (x1, y1), (x2, y2) and (x3, y3), write a Python program to check if 
#they are Collinear.

def collinear(x1, y1, x2, y2, x3, y3):
 #Slope rule for colinearity   
    if ((y3 - y2)*(x2 - x1) == (y2 - y1)*(x3 - x2)): 
        print ("Collinear.")
    else:
        print ("Not collinear.")
  
x1, x2, x3, y1, y2, y3 = 1, 1, 0, 1, 6, 9
collinear(x1, y1, x2, y2, x3, y3)