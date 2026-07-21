class car :
    def __init__(self):
        self.brand = ('')
        self.model = 0

    def setbrand(self,b):
        self.brand = b

    def getbrand(self):
        return self.brand

    def setmodel(self,m):
        self.model = m

    def getmodel(self):
        return self.model


class Electriccar(car):
    def __init__(self):
        self.charge_battery = 0
        self.eco_mode = 0
        self.fast_charge = 0

    def setcharge_battery(self,b):
        self.charge_battery = b
    def getcharge_battery(self):
        return self.charge_battery
    def seteco_mode(self,e):
        self.eco_mode = e
    def geteco_mode(self):
        return self.eco_mode
    def setfast_charge(self,f):
        self.fast_charge = f
    def getfast_charge(self):
        return self.fast_charge

E = Electriccar ()
E.setbrand("TATA")
E.setmodel("NEXON")
E.setcharge_battery("Range : 80kw")
E.seteco_mode("ecomodeactivated")
E.setfast_charge("fast charging enable")

print(" brand name",E.getbrand())
print("model name",E.getmodel())
print("charge_battery",E.getcharge_battery())
print("eco_mode",E.geteco_mode())
print("fast charging",E.getfast_charge())


