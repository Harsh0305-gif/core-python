class shape:
    def __init__(self,color,boderwidth):
        self.color = color
        self.boderwidth = boderwidth

    def setcolor(self,color):
         self.color = color
    def getcolor(self):
        return self.color
    def setboderwidth(self,boderwidth):
        self.boderwidth = boderwidth
    def getboderwidth(self):
        return self.boderwidth

class reactangle(shape):
    def __init__(self,length=0,width=0,color='',boderwidth=0):
        self.length = length
        self.width = width
        super().__init__(color,boderwidth)

    def setlength(self,l):
        self.length = l
    def getlenth(self):
        return self.length
    def setwidth(self,w):
        self.width = w
    def getwidth(self):
        return self.width
r = reactangle(20,20,'red',23)
print("rectangle:")
print("lenth",r.getlenth())
print("width",r.getwidth())
print("color=",r.getcolor())
print("boderwidth=",r.getboderwidth())
