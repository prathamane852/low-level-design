"""
Abstraction: expose WHAT an object does, hide HOW it does it.

The driver only knows the Car interface (start, accelerate, brake, stop).
The engine, fuel injection, gear shifting etc. are hidden inside each car.
"""

from abc import ABC, abstractmethod

# ABC = Abstract Base Class means that this class cannot be instantiated directly, 
# only subclasses can be instantiated. 
# it defines a common interface for all subclasses to implement.
# Subclass means that a class inherits from another class. 
# In this case, PetrolCar and ElectricCar inherit from Car.
# common interface means that all subclasses must implement the same methods
# abstractmethod decorator is used to declare methods that must be implemented by subclasses.

class Car(ABC):
    """Abstract class: defines the interface every car must provide."""

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.speed = 0

    @abstractmethod
    def start_engine(self) -> None: ...

    @abstractmethod
    def accelerate(self, amount: int) -> None: ...

    @abstractmethod
    def brake(self, amount: int) -> None: ...

    @abstractmethod
    def stop_engine(self) -> None: ...

    # Concrete method shared by all cars
    def display(self) -> None:
        print(f"{self.brand} {self.model} | speed: {self.speed} km/h")


class PetrolCar(Car):
    def start_engine(self) -> None:
        # Hidden details: ignition, fuel pump, spark plugs...
        self._inject_fuel()
        self._ignite_spark_plugs()
        print(f"{self.brand} {self.model}: Vroom! Petrol engine started.")

    def accelerate(self, amount: int) -> None:
        self._shift_gear()
        self.speed += amount
        print(f"Accelerating to {self.speed} km/h")

    def brake(self, amount: int) -> None:
        self.speed = max(0, self.speed - amount)
        print(f"Braking to {self.speed} km/h")

    def stop_engine(self) -> None:
        self.speed = 0
        print(f"{self.brand} {self.model}: Petrol engine stopped.")

    # Internal (hidden) helpers — the user never calls these
    # These methods are private to the PetrolCar class and are not part of the Car interface.
    def _inject_fuel(self) -> None:
        pass

    def _ignite_spark_plugs(self) -> None:
        pass

    def _shift_gear(self) -> None:
        pass


class ElectricCar(Car):
    def start_engine(self) -> None:
        # Hidden details: battery check, motor controller...
        self._check_battery()
        print(f"{self.brand} {self.model}: *silent* Electric motor ready.")

    def accelerate(self, amount: int) -> None:
        self.speed += amount
        print(f"Instant torque! Speed is now {self.speed} km/h")

    def brake(self, amount: int) -> None:
        self.speed = max(0, self.speed - amount)
        print(f"Regenerative braking to {self.speed} km/h (battery charging)")

    def stop_engine(self) -> None:
        self.speed = 0
        print(f"{self.brand} {self.model}: Motor powered off.")

    # This method is private to the ElectricCar class and is not part of the Car interface.
    def _check_battery(self) -> None:
        pass


def drive(car: Car) -> None:
    """The driver works with ANY Car without knowing its internals."""
    car.start_engine()
    car.accelerate(40)
    car.accelerate(30)
    car.brake(20)
    car.display()
    car.stop_engine()
    print("-" * 40)


# if __name__ == "__main__": means that the code inside this block will only be executed 
# if the script is run directly, not if it is imported as a module in another script.
# in easy words, it is a way to prevent certain code from being run when the module is imported.
if __name__ == "__main__":
    drive(PetrolCar("Toyota", "Corolla"))
    drive(ElectricCar("Tesla", "Model 3"))

    # Car("Generic", "X")  # TypeError: can't instantiate abstract class
