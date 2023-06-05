import math


class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area_calculation(self):
        
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

    

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def area_calculation(self):
        area = ((self.base * self.height)/2)
        return area
    

        
        
class Square:
    def __init__(self,width):
        self.width = width
        
    def area_calculation(self):
        area = self.width * self.width
        return area
        
        
    