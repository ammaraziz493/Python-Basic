class Person:
    name = "Ammar Aziz"
    occupation = "Software Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
a.name = "Harry"
print(a.name)
a.info()
