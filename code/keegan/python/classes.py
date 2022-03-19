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

# --------------------------------------------------------------------- #

# define a class to encapsulate the data and methods for a Point

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


    def __str__(self):
        '''The string returned from this method will act as the string 
        representation of every instance of this class'''
        return f"Point: ({self.x}, {self.y})"

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
# -------------------------------------------------------------------- #
