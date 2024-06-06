class Dog:
    _number = 0
    # _protected = "I am a protected variable"
    def __init__(self, name):
        self.name = name
        Dog._number += 1
        self.dognumber = Dog._number


        def bark(self):
            print(f"{self.name} says woof!")

jack = Dog("jack")
print(jack.dognumber)
            

    