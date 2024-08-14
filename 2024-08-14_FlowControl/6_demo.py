a = 3
b = 2
c = 1

def demo():
    y = (a+b+c)
    
demo

# defines the value of pi
pi = 3.14159

# Calculates the area of a circle for a given radius
def calculate_circle_area(radius):
    return pi*radius**2

r = int(input('Enter the radius of the circle: '))
area = calculate_circle_area(r)
print(area)