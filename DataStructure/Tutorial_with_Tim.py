# object oriented programming in python


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def meow(self):
        return "meow"
    def bark(self):
        print("bark")


d = Dog("tim", 12)
d.bark()
print(type(d))



