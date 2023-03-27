class MyClass:
    name = "Mittal Trivedi"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name,age)
    
    def sum(self,a,b):
        print(a+b)
    
x = MyClass("John",27)
print(x.name)
del x.name
print(x.age)
x.sum(10,20)

