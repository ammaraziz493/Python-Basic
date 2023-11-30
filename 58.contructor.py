class Person:
    def __init__(self, n, o):
        print("Hey  i am there")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person("Ammar" , " Developer")
a.info()
b = Person("Ali", "Hr")
b.info()
