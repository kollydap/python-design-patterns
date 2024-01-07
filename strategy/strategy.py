from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self):
        self.quack_behavior = None
        self.fly_behavior = None

    @abstractmethod
    def display(self):
        pass

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

class IQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class Quack(IQuackBehavior):
    def quack(self):
        print("I quack")

class Squeak(IQuackBehavior):
    def quack(self):
        print("I squeak")

class MuteQuack(IQuackBehavior):
    def quack(self):
        print("I do not quack")

class IFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(IFlyBehavior):
    def fly(self):
        print("I am flying with wings")

class FlyWithTail(IFlyBehavior):
    def fly(self):
        print("I am flying with tail")

class DoNotFly(IFlyBehavior):
    def fly(self):
        print("I cannot fly")

class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def change_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def display(self):
        print("I am a Mallard Duck")

# Example Usage
mallard_duck = MallardDuck()
mallard_duck.display()
mallard_duck.perform_quack()
mallard_duck.perform_fly()

mallard_duck.change_quack_behavior(Squeak())
mallard_duck.perform_quack()
