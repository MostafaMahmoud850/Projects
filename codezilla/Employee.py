class Employee:
    def __init__(self, name, age, department, is_manager, rating, salary):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
        self.rating = rating
        self.salary = salary

    def is_excellent(self):
        if self.rating >= 4.5:
            return True
        else:
            return False
        
    def bonus(self):
        if self.age == 60:
            self.salary += 500
            print("salary is increased to " + str(self.salary))
        else:
            print("no bonus add, salary is still " + str(self.salary))

        