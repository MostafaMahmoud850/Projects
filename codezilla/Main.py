from Employee import Employee

employee1 = Employee("islam", 50, "codezilla", True, 5, 1500)
employee2 = Employee("ibrahim", 60, "facebook", False, 3.5, 500)

print(employee1.is_excellent())
print(employee2.is_excellent())

print(employee1.salary)
employee1.bonus()
print(employee2.salary)
employee2.bonus()