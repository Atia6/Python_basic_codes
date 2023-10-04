#Write Python program to demonstrate Multiple Inheritance.

#When a class can be derived from more than one base class this type of inheritance
#  is called multiple inheritances. In multiple inheritances, all the features of the
#  base classes are inherited into the derived class. 

# Base class1
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
# Base class2
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
# Derived class
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
# Driver's code
s1 = Son()
s1.fathername = "Rahim"
s1.mothername = "Mala"
s1.parents()