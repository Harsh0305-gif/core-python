class person:
    def __init__(self):
        print("person class")
        self.__name = None
        self.__dob  =None
        self.__address = None

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self,dob):
        self.__dob = dob

    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address
p= person()
p.set_name("harshit")
p.set_dob("2004,08,05")
p.set_address("naryiakheda")

print("name:",p.get_name())
print("dob:",p.get_dob())
print("addresss:",p.get_address())
