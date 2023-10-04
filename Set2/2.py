# Defining base class
class Parent():
      
    # Constructor
    def __init__(self):
        self.value = "Base class method"
          
    # Parent's show method
    def show(self):
        print(self.value)
          
# Defining derived class
class Child(Parent):
      
    # Constructor
    def __init__(self):
        self.value = "Base class method overridden"
          
    # Child's show method
    def show(self):
        print(self.value)
          
          
# Driver's code
obj1 = Parent()
obj2 = Child()
  
obj1.show()
obj2.show()
