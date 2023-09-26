class vehicle():
  def __init__(self , name_of_vehicle , max_speed , average_of_vehicle):
    self.name_of_vehicle = name_of_vehicle
    self.max_speed = max_speed
    self.average_of_vehicle=average_of_vehicle

class Car(vehicle):
  def __init__(self , name_of_vehicle , max_speed , average_of_vehicle ):
    super().__init__(name_of_vehicle , max_speed , average_of_vehicle)
    # self.capacity = int(input("enter the capacity"))
  def seating_capacity (self ,capacity):
    self.capacity = int(input("enter the capacity"))
    return (f"the name of the vehicle is {self.name_of_vehicle} and its seating capacity is {self.capacity} ")

v1 = Car("nissan" , 240 , 15)
print(v1.seating_capacity(capacity=0))

     
# multiple inheritance is the inheritance in which one child class inherit from two or more different  parent class

class one():
  def __init__(self , number):
    self.number = number

class two():
  def __init__(self, alphabet):
    self.alphabet = alphabet
    
class three (one , two):
  def __init__(self , name , number , alphabet):
    one.__init__(self , number)
    two.__init__(self , alphabet)
    self.name = name
    
  def show(self):
   return (f"the number() is {self.number} , alphabet is {self.alphabet} and the name is {self.name}")


first = three("akshat",22 , "A")
print(first.show())

class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.__age = age
    self.gender = gender

  def say_hello(self):
    print(f"Hello, {self.name}.")

  def is_adult(self):
   return self.__age >= 18
   
  def get_age(self):
   return self.__age   



class Student(Person):
  def __init__(self, name, age, gender, student_id, course):
   super().__init__(name, age, gender)
   self.student_id = student_id
   self.course = course

def study(self):
   print(f"{self.__name} is studying {self.course}.")

class Teacher(Person):
  def __init__(self, name, age, gender, teacher_id, subject):
   super().__init__(name, age, gender)
   self.teacher_id = teacher_id
   self.subject = subject

def say_hello(self):
   print(f"Hello, I'm {self.__name}, your {self.subject} teacher.")