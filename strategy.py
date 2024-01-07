class Duck:
    def __init__(self, name: str):
        self.name = name

    def swim(self):
        print("swimming duck")


class RubberDuck(Duck):
    def __init__(self, color: str):
        self.color = color
r1 = RubberDuck(color="Red")
r1.swim()
