class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def DetailEmployee(self):
        print(f"The name of employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showlanguage(self):
        print("The default language is Python")


a = Employee("Ammar", "1")
a.DetailEmployee()
a2 = Programmer("ali","2")
a2.DetailEmployee()
a2.showlanguage()
