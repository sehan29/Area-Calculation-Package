import math


class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area_calculation(self):
        
        area = (math.pi * self.radius * self.radius)
        area = round(area,2)
        """         print(area) """
        return area
        
    def surface_area(self):
        
        area = (math.pi * self.radius * self.radius)
        area = round(area,2)
        """         print(area) """
        return area
        
    
    
    
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area_calculation(self):
        area = (self.width * self.height)
        area = round(area,2)
        """         print(area) """
        return area
        
    def surface_area(self):
        
        surface_area = (self.width * self.height)
        surface_area = round(surface_area,2)
        return surface_area
    

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def area_calculation(self):
        area = ((self.base * self.height)/2)
        return area
    
    def surface_area(self):
        pass
        
        
class Cylinder:
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
        
    def area_calculation(sekf):
        pass
        
    
    def surace_area(self):
        surface_area_cylinder = ((2 * math.pi * self.radius * self.radius) + (2 * math.pi * self.radius * self.height))
        surface_area_cylinder = round(surface_area_cylinder,2)
        return surface_area_cylinder
        
        
    