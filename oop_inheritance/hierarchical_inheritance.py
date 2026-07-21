class shape:
    def __init__(self,color = '',boderwidth = 0):
        self.color = color
        self.boderwidth = boderwidth

    def getcolor(self):
        return self.color
    def getboderwidth(self):
        return self.boderwidth

class Reactangle(shape):
    def __init__(self,length = 0,width = 0,color = '',boderwidth = 0):
        self.length = length
        self.width =width
        super().__init__(color, boderwidth)
    def getlength(self):
        return self.length
    def getwidth(self):
        return self.width

class circle(shape):
    def __init__(self, radius=0,width=0,  color='',borderwidth=0):
        self.radius = radius
        super().__init__(color,borderwidth)
    def getradius(self):
        return self.radius


r =Reactangle(21,23,'green',33)
print("reactangle")
print("length",r.getlength())
print("width",r.getwidth())
print("color",r.getcolor())
print("boderwidth",r.getboderwidth())

c = circle(23,21,"blue",21)
print("circle")
print("radius",c.getradius())
print("color",c.getcolor())
print("boderwidth",c.getboderwidth())


