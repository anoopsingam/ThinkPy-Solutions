# Write an init method for the Point class that takes x and y as optional
# parameters and assigns them to the corresponding attributes.

# Current Status: Complete

#init method meaning 
#The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created. Like methods, a constructor also contains collection of statements(i.e. instructions) that are executed at time of Object creation.


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print "x =", self.x, ",",
        print "y =", self.y

point = Point()
point.print_point()

point = Point(10)
point.print_point()

point = Point(20, 30)
point.print_point()
