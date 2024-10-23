# Write a Python function circle_area(radius) that takes the radius of a circle and 
# returns the area of the circle. (Use the formula: Area = π × radius², assume π = 3.1416).

def circle_area(radius):
    pi = 3.1416
    return pi*(radius**2)

result = circle_area(5)
print(result)
