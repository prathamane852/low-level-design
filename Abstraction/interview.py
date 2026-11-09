# ABSTRACTION — show WHAT an object does, hide HOW it does it.
# Real life: a driver uses the steering wheel, pedals and key,
# without knowing how the engine works inside.
#
# In Python: use ABC (Abstract Base Class) + @abstractmethod.
#   - An abstract class CANNOT be instantiated directly.
#   - Every subclass MUST implement all abstract methods,
#     otherwise creating that subclass also raises TypeError.

from abc import ABC, abstractmethod


class Car(ABC):                      # abstract class = the "contract" / interface
    @abstractmethod
    def start(self): ...             # WHAT every car must do (no HOW here)

    @abstractmethod
    def stop(self): ...

    # Normal (concrete) method — NO @abstractmethod:
    #   - subclasses inherit it automatically, they don't have to write it
    #   - subclasses CAN still override it if they want different behaviour
    #   - Car() is still not allowed, because start/stop are still abstract
    #   (If an ABC has ZERO abstract methods, it CAN be instantiated. means it is not abstract anymore. 
    # example is class Car(ABC): pass)
    def honk(self):
        print("Beep beep!")


class PetrolCar(Car):                # concrete class = provides the HOW
    def start(self):
        print("Petrol car: ignition + fuel injection -> engine started")

    def stop(self):
        print("Petrol car stopped")


class ElectricCar(Car):
    def start(self):
        print("Electric car: battery check -> motor started")

    def stop(self):
        print("Electric car stopped")


def drive(car: Car):                 # depends only on the abstraction, not the details
    car.start()
    car.honk()                       # inherited from Car, not defined in subclasses
    car.stop()


if __name__ == "__main__":
    drive(PetrolCar())
    drive(ElectricCar())
    # Car()  -> TypeError: Can't instantiate abstract class Car


# Interview one-liners:
# - Abstraction = hide implementation, expose only essential behaviour.
# - Abstraction vs Encapsulation: abstraction hides COMPLEXITY (design level),
#   encapsulation hides DATA (bundling data + methods, restricting access).
# - Benefit: caller code (drive) works with any new Car type without changes.
