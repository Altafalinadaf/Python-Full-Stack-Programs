class Student:
    def __init__(self,name,cls):
        self.name=name
        self.cls=cls
    
    def hello(self):
        print("Hello EveryOne ")

s=Student('Khaleel',9)
s.hello()