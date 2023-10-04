#Write Python program to calculate the Arc Length of an Angle by assigning values to the 
#radius and angle data attributes of the class ArcLength. 

#import math package to use math.pi for the value of PI 
import math     
#create a function to calculate the arc length.
def Arclength():
    # take input radius and angle .
    r= float(input("Enter the radius of circle: "))
    Angle = float(input("Enter the angle value: "))
    # checking for the angle validation 
    if Angle >= 360:
        print("Invalid angle entered ")
        return
    #calculate  arc length.
    Arc_length = 2*(math.pi*r) * (Angle/360)
    return Arc_length
#accessing and printing arc length
arc_length = Arclength()
print(arc_length)