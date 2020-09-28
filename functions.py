class Student:
    def __init__(self):       #Default constructor,
        self.id=10
        self.name='sush'
        print("This is constructor")
    def display(self):
        print(self.id)
        print(self.name)
obj1=Student()                   # constructor gets called automattically when we create object for that class
obj1.display()                    # accsessing members of class using ref variable,obj1 is ref variable