class Rombus:
    def __init__(self, side_a, conner_a):
        self.side_a = side_a
        self.conner_a = conner_a
        self.conner_b = 180 - conner_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                print("Side must be greater than 0.")
            else:
                super().__setattr__(name, value)
        elif name == "conner_a":
            if 0 <= value >= 180:
                print(f"Conner '{name}' must be between 0 and 180 degrees.")
            else:
                super().__setattr__(name, value)
                self.__dict__["conner_b"] = 180 - value
        elif name == "conner_b":
            if 0 <= value >= 180:
                print(f"Conner '{name}' must be between 0 and 180 degrees.")
            else:
                 if self.conner_a + value != 180:
                    print("The sum of conner must be 180 degrees.")
                else:
                    super().__setattr__(name, value)
                    self.__dict__["conner_a"] = 180 - value

# Testing the code
romb = Rombus(10, 99)
print(romb.conner_a)
print(romb.conner_b)

romb.conner_a = 70
print(romb.conner_b)
