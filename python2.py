class Dog:
#    class attribute, private and public, @ property.
    _number = 0
    # _protected = "I am a protected variable"
    def __init__(self, name):
        self.name = name
        Dog.number += 1
        self.__dognumber = Dog.number


#         def bark(self):
#             print(f"{self.name} says woof!")

# jack = Dog("jack")
# print(jack.dognumber)

# @dognumber.setter
# def dognumber(self, number):
#     self.__dognumber = number



#     def bark(self):
#         print(*(self.name)says woof!*)



class account:

    @ get property
    def get__balance(self)
    return self balance
    
              