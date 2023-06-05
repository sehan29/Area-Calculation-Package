import math

class Cube:
    
    def __init__(self,width_of_cube):
        self.width_of_cube = width_of_cube
        
    def surface_area(self):
        
        area = (self.width_of_cube * self.width_of_cube * 6)
        area = round(area,2)
        return area


class Sphere:
    
    def __init__(self,radius):
        self.radius = radius
    
    def surface_area(self):
        
        area = (4 * math.pi * self.radius * self.radius)
        area = round(area,2)
        return area


class Cylinder:
    
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    
    def surface_area(self):
        
        area = ((2 * math.pi * self.radius * self.radius) +(2 * math.pi * self.radius * self.height))
        area = round(area,2)
        return area