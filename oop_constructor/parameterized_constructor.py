class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name
    def getage(self):
        return self.age

s = student("Harshit",21)
print("name",s.getname())
print("age",s.getage())
