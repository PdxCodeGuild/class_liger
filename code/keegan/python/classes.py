'''
OOP (Object-Oriented Programming)
Bundling variables and functions that work on those variables within one unit (Class).
Thinking of a program in terms of objects and their relationships instead of a bunch of
independent functions.


Three Pillars of OOP
Encapusulation - Hiding the internals of a class, specifying and interface by
                 which other code can use the class ('has-a' relationship)

Inheritance - Deriving one type from another type ('is-a' relationship)

Polymorphism - The ability to use one type as another type
'''


# dir(object) - return a list of all the members of the class from which the object is derived
# print(dir(''))

'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__forma
t__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__in
it__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__
ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr_
_', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'e
ncode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'issp
ace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'remov
eprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip
', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

# -------------------------------------------------------------------------------------------- #

# all datatypes are of the type 'type'
# print(type(str)) # <class 'type'>
# print(type(int)) # <class 'type'>
# print(type(list)) # <class 'type'>
# print(type(dict)) # <class 'type'>
# print(type(tuple)) # <class 'type'>
# print(type(None)) # <class 'NoneType'>

# --------------------------------------------------------------------------------------------- #

# Describe two cartesian points (x, y)
# Calculate the distance between them


import math
def distance(p1, p2):
    # difference in x
    dx = p1[0] - p2[0]
    # difference in y
    dy = p1[1] - p2[1]

    # return the distance
    return math.sqrt(dx**2 + dy**2)


# p = [x, y]
p1 = [5, 2]
p2 = [8, 4]

# print(distance(p1, p2)) # 3.605551275463989

# --------------------------------------------------------------------- #


def distance(p1, p2):
    # difference in x
    dx = p1['x'] - p2['x']
    # difference in y
    dy = p1['y'] - p2['y']

    # return the distance
    return math.sqrt(dx**2 + dy**2)


# More readability with a dictionary
p1 = {'x': 5, 'y': 2}
p2 = {'x': 8, 'y': 4}

# print(distance(p1, p2)) # 3.605551275463989

# --------------------------------------------------------------------- #

# define a class to encapsulate the data and methods for a Point

# class - the blueprint from which an object of a certain type is created
# instance - object created from the class and given specific properties

my_string = str()

# my_point = Point()

class Point:
    def __init__(self, x, y):
        # create a class attribute called 'self.x' which every instance of a Point will now have
        self.x = x
        # create a class attribute called 'self.y' which every instance of a Point will now have
        self.y = y


    def distance(self, p2):
        '''calculate the distance between two Point objects, self (p1) and p2'''
        # difference in x
        dx = self.x - p2.x
        # difference in y
        dy = self.y - p2.y

        # return the distance
        return math.sqrt(dx**2 + dy**2)

    # static methods belong to the class itself and not the specific instances
    @staticmethod
    def scale_point(point, scalar_value):
        '''Multiply the x and y values of a point by the scalar value return a new Point object'''
        x = point.x * scalar_value
        y = point.y * scalar_value
        return Point(x, y)

    def __str__(self):
        '''The string returned from this method will act as the string 
        representation of every instance of this class'''
        return f"Point: ({self.x}, {self.y})"

    def __eq__(self, p2):
        '''Return True if the x and y coords of both points are equal'''
        return self.x == p2.x and self.y == p2.y

    def __add__(self, p2):
        '''Return the sum of the x and y values of each point'''
        new_x = self.x + p2.x
        new_y = self.y + p2.y

        return Point(new_x, new_y)

# print(type(Point)) # <class 'type'> # created a datatype

# initialize or 'instanciate' the Point class to create a Point object
p1 = Point(5, 2)

# print the x and y coords of p1
# print(p1.x) # 5
# print(p1.y) # 2
# print(p1) # Point: (5, 2)

# initialize another Point object
p2 = Point(8, 4)

# print the x and y coords of p1
# print(p2.x) # 8
# print(p2.y) # 4
# print(p2) # Point: (8, 4)


# calculate the distance between two points
# print(p1.distance(p2)) # 3.605551275463989

# call the class method to scale p1.x and p1.y by 2
# print(Point.scale_point(p1, 2)) # Point: (10, 4)

# check the equality of two points (__eq__)
p3 = Point(3, 3)
p4 = Point(3, 3)

# print(p3 == p4) # True
# print(p3 == p1) # False


# Add two points together (__add__)
# print(p3 + p4) # Point: (6, 6)

# -------------------------------------------------------------------- #

# Classes can have private variables which are denoted with a 
# double underscore before their name which aren't available outside the class

class PrivatePoint:
    def __init__(self, x, y):
        self.__x = x # double underscore signifies a private variable
        self.__y = y # double underscore signifies a private variable

    def distance(self, p2):
        '''calculate the distance between two Point objects, self (p1) and p2'''
        # difference in x
        dx = self.__x - p2.__x
        # difference in y
        dy = self.__y - p2.__y

        # return the distance
        return math.sqrt(dx**2 + dy**2)

    


priv3 = PrivatePoint(8,5)
priv4 = PrivatePoint(1,3)
# print(priv3.__x) # AttributeError: 'PrivatePoint' object has no attribute '__x'
# print(priv3.__y) # AttributeError: 'PrivatePoint' object has no attribute '__y'

# print(priv3.distance(p4))

# private attributes are still available if absolutely necessary
# print(priv3.__dict__) # {'_PrivatePoint__x': 8, '_PrivatePoint__y': 5}

# ------------------------------------------------------------------------ #


class Circle:
    def __init__(self, radius, center_x, center_y):
        self.radius = radius

        self.center = Point(center_x, center_y) # encapsulation

    def __str__(self):
        return f"Circle of radius {self.radius}, centered at ({self.center.x}, {self.center.y})"
    
circle1 = Circle(10, 5, 6)

# the circle doesn't have x,y coordinates, but the Point object at its center does
# print(circle1.x) # AttributeError: 'Circle' object has no attribute 'x'

# print(circle1.center.x) # 5
# print(circle1.center.y) # 6

# print(circle1) # Circle of radius 10, centered at (5, 6)

# ---------------------------------------------------------------------------------- #

class Person:
    def __init__(self, first_name:str, last_name:str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self):
        return "Hello"

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return f"{self.get_full_name()} - {self.age} years"

class Student(Person): # inheritance - each Student object gets all the qualities of a Person class
    def __init__(self, first_name:str, last_name:str, age:int, subjects:list[str]=[]):
        # instead of creating all the same class variables as in the Person class,
        # call the 'super' function instead to call the Person class's __init__ method
        super().__init__(first_name, last_name, age)

        # only students will have a list of subjects
        self.subjects = subjects

    # override the say_hello method from the Person class
    def say_hello(self):
        return "Hey, what's up?"

    def __str__(self):
        return f"{self.get_full_name()} - subjects: {self.subjects}"
    
    def __repr__(self):
        '''The return value will be used when the object needs to represented in the code'''
        return f"{self.get_full_name()} - subjects: {self.subjects}"

class Instructor(Person):
    def __init__(self, first_name:str, last_name:str, age:int, subject:str, students:list=[]):
        super().__init__(first_name, last_name, age)

        self.subject = subject
        self.students = students

    def __str__(self):
        return f"{self.get_full_name()} - {self.subject} - students: {self.students}"

    def __repr__(self):
        '''return this value whenever a code representation is needed of the object'''
        return f"{self.get_full_name()} - {self.subject} - students: {self.students}"


person_1 = Person('Bilbo', 'Baggins', 111)
# print(person_1) # Bilbo Baggins - 111 years

person_2 = Person('Gandalf', 'the Grey', 999)
# print(person_2) # Gandalf the Grey - 999 years

# print(f"{person_1.get_full_name()} says {person_1.say_hello()}") # Bilbo Baggins says Hello
# print(f"{person_2.get_full_name()} says {person_2.say_hello()}") # Gandalf the Grey says Hello


# --------------- #

student_1 = Student('Bilbo', 'Baggins', 111, ['burglary', 'adventuring'])
student_2 = Student('Gandalf', 'the Grey', 999, ['wizardry', 'adventuring'])
student_3 = Student('Frodo', 'Baggins', 75, ['burglary', 'adventuring'])

# print(person_1.say_hello()) # Hello
# print(student_1.say_hello()) # Hey, what's up?

instructor_1 = Instructor('Keegan', 'Good', 33, 'Python', students=[student_1, student_2, student_3])
print(instructor_1)