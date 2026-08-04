import threading
from threading import *
class hi(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range (1,11):
            print(self.name,i)

t1 =hi('abc')
t2 = hi('xyz')

t1.start()
t2.start()