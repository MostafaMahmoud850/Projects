# # instance method
# class Student:
#     no_of_students = 0
#     def __init__(self, name, age=0, courses="none") -> None:
#         self.__name = name
#         self.__age = age
#         self.__courses = courses
#         Student.no_of_students +=1

    # def get_name(self):
    #     return self.__name

    # def set_name(self, new_name):
    #     self.__name = new_name   

    # def get_age(self):
    #     return self.__age

    # def set_age(self, new_age):
    #     self.__age = new_age  

    # def describe(self):
    #     print(f"my name is {self.__name} and my age is {self.__age}.")
    
    # def is_old(self, num):
    #     if self.__age <= num:
    #         print("student is not old.")
    #     else:
    #         print("student is old.")

# student1 = Student("mostafa", 25, ['SQl', 'Python'])
# student2 = Student("mostafa", 25, ['PowerBI', 'Excel'])
# print(id(student1), id(student2))
# print(Student.no_of_students, student1.no_of_students)
# student1.describe()
# student1.is_old(50)
# student1.name = "mohamed"
# student1.grade = "fifth"
# print(student1.grade)
# print(student1.name)
# print(student1.get_name())
# print(student1.__name) ---> AttributeError: 'Student' object has no attribute '__name'

# student1.set_name("mohamed")
# student1.set_age(50)
# student1.describe()


# # class method
# from datetime import date
# class Student:

#     def __init__(self, name, age= 0) -> None:
#         self.name = name
#         self.age = age

#     def describe(self):
#         print(f"my name is {self.name} and my age is {self.age}.")

#     @classmethod
#     def init_from_birth_year(cls, name, birthyear):
#         return cls(name, date.today().year - birthyear)
    
# # student1 = Student("islam", 20)
# # student2 = Student.init_from_birth_year("ahmed", 1993)
# # student2.describe()

# class Pizza:
#     def __init__(self, ingredients) -> None:
#         self.ingredients = ingredients

#     @classmethod
#     def veg(cls):
#         return cls(['mushrooms', 'olives', 'onions'])
    
#     @classmethod
#     def margherita(cls):
#         return cls(['mozarella', 'sauce'])
    
#     def __str__(self) -> str:
#         return f"pizza ingredients are {self.ingredients}"
    
# pizza1 = Pizza(['tomatoes', 'olives'])
# pizza2 = Pizza.veg()
# pizza3 = Pizza.margherita()
# print(pizza1, pizza2, pizza3)
# # print(dir(Pizza))


# # staticmethod

# class Math:

#     @staticmethod
#     def add(x, y):
#         return x + y
    
#     @staticmethod
#     def add5(num):
#         return num + 5

#     @staticmethod
#     def add10(num):
#         return num + 10
    
#     @staticmethod
#     def PI():
#         return 3.14
    
# x = Math.add(5, 10)
# y = Math.add5(x)
# z = Math.add10(y)
# print(x, y, z)

# class Pizza:
#     def __init__(self, radius, ingredients) -> None:
#         self.radius = radius
#         self.ingredients = ingredients

#     def __str__(self) -> str:
#         return f"pizza ingredients are {self.ingredients}"
    
#     def area(self):
#         return Pizza.circle_area(self.radius)
    
#     @staticmethod
#     def circle_area(r):
#         return r ** 2 * Math.PI()
    
# p = Pizza(6, ['mozzarella', 'tomatoes'])
# print(p.area())
# print(Pizza.circle_area(4))
# print(Pizza.circle_area(10))

# class Dates:
#     def __init__(self, date) -> None:
#         self.__date = date

#     def get_date(self):
#         return self.__date
    
#     @staticmethod
#     def to_dash_date(date):
#         return date.replace("/", "-")
    
# date = Dates("15-12-2016")
# date_from_DB = "15/12/2016"
# date_with_bash = Dates.to_dash_date(date_from_DB)
# print(date_with_bash)

# if(date.get_date() == date_with_bash):
#     print("Equal")
# else:
#     print("Unequal")


# # inheretance and polymerphism

# from datetime import date
# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display(self):
#         return f"name is {self.name} and age is {self.age}"
    
#     @classmethod
#     def init_from_birth_year(cls, name, birthyear, extra=None):
#         return cls(name, date.today().year - birthyear, extra)

# class Man(Person):
#     gender = "Male"
#     no_of_men = 0

#     def __init__(self, name, age, voice):
#         super().__init__(name, age)
#         self.voice = voice
#         Man.no_of_men += 1


#     def display(self):
#         string = super().display()
#         return string + f" and voice is {self.voice} and gender is {self.gender}."
    
# man = Man("islam", 30, "hard")
# print(man.display())
# print(man.no_of_men)



# class Women(Person):
#     gender = "Female"
#     no_of_women = 0

#     def __init__(self, name, age, hair) -> None:
#         super().__init__(name, age)
#         self.hair = hair
#         Women.no_of_women += 1

#     def display(self):
#         string = super().display()
#         return string + f" and hair is {self.hair} and gender is {self.gender}."
    
# women = Women("somaya", 30, "curly")
# print(women.display())
# print(Women.no_of_women)

# man = Man.init_from_birth_year("islam", 1990, "hard")
# print(man.display())

# women = Women.init_from_birth_year("somaya", 1980, "culry")
# print(women.display())

# print(isinstance(women, Women))
# print(isinstance(man, Man))
# print(isinstance(women, Man))
# print(isinstance(man, Women))
# print(isinstance(women, Person))
# print(isinstance(man, Person))



# # abstraction

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Square(Shape):
#     def __init__(self, side) -> None:
#         self.__side = side

#     def area(self):
#         return self.__side * self.__side
    
#     def perimeter(self):
#         return self.__side * 4
    
# class Rect(Shape):
#     def __init__(self, length, width) -> None:
#         self.__length = length
#         self.__width = width

#     def area(self):
#         return self.__length * self.__width
    
#     def perimeter(self):
#         return (self.__length + self.__width) * 2
        

# square = Square(10)
# print(f"square area is {square.area()} and perimeter is {square.perimeter()}.")
# rect = Rect(5, 3)
# print(f"rectangle area is {rect.area()} and perimeter is {rect.perimeter()}.")    



# # Dunder methods

# class Man():
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def __add__(self, other):
#         names = self.name + " and " + other.name
#         ages = self.age + other.age
#         return f"names combined are {names} and sum of ages are {ages}."
    
#     def __lt__(self, other):
#         return self.age < other.age
    
#     def display(self):
#         return f"name is {self.name} and age is {self.age}."
    

# # man = Man("islam", 20)
# man = Man("islam", 60)
# man2 = Man("ahmed", 30)
# print(man + man2)
# print(man < man2)




