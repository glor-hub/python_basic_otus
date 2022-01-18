"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):
    engine = (0,0)

    def set_engine(self, engine):
       self.engine=engine

if __name__ == '__main__':
    r=Car(4,5,6)
    r.set_engine(Engine(2,3))
    print(r.__dict__.values())
