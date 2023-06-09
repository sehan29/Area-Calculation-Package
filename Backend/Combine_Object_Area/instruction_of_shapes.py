import Backend.Area.obstacle_class as my_class


def circle_instruction():
    
    radius_of_circle = 0
    print("* To calculate the area of a circle, You Have to input Radius of Circle")
    print("* Area = π * r^2")
    print("* r = Radius (m)\n")
    
    try:
        radius_of_circle = float(input("Enter The Radius Of Circle : "))
        k = my_class.Circle(radius_of_circle)
        area_of = k.area_calculation()
        return area_of        
        
    
    except:
        print("---- Pleace Enter The Decimal Number ----")
        


def cylinder():
    

    
    print("* To calculate the area of a Cylinder, You Have to input Radius of Cylinder and Height")
    print("* Surface Area = 2πr^2 + 2πrh")
    print("* r = Radius (m)")
    print("* h = Height (m)\n")
    
    try:
        radius_of_circle = float(input("Enter The Radius Of Cylinder : "))
        height_of_cycilder = float(input("Enter The Heght Of Cylinder : "))
    
    except:
        print("---- Pleace Enter The Decimal Number ----")
    
    

def rectangle():
    
    width_of_rectangle = 0
    height_of_rectangle = 0
    area_of_rectangle = 0
    print("=---------------=")
    print("=               =")
    print("=               =")
    print("=               =")
    print("=---------------=\n")
    print("* To calculate the area of a Rectangle, You Have to input Width and Height")
    print("* Surface Area = Rectangle Width x Rectangle Height")
    print("* w = Width (m)")
    print("* h = Height (m)\n")
    
    try:
        width_of_rectangle = float(input("Enter The Width of Rectangle : "))
        height_of_rectangle = float(input("Enter The Heght Of Rectangle : "))
        rectangle_obj = my_class.Rectangle(width_of_rectangle, height_of_rectangle)
        area_of_rectangle = rectangle_obj.area_calculation()
        
        print(area_of_rectangle)
        
        return area_of_rectangle 
        

    
    except:
        print("---- Please Enter The Decimal Number ----")
    


def instruction_square():
    
    width_of_rectangle = 0
    height_of_rectangle = 0
    
    print("* To calculate the area of a Square, You Have to input Width and Height")
    print("* Surface Area = Square Width x Square Height")
    print("* w = Width (m)")
    print("* h = Height (m)\n")
    
    try:
        width_of_rectangle = float(input("Enter The Width Of Rectangle : "))
        height_of_rectangle = float(input("Enter The Heght Of Rectangle : "))
        
    except:
        
        print("---- Please Enter The Decimal Number ----")
        
    
def instruction_triangle():
    
    base_of_triangle = 0
    height_of_triangle = 0
    area_of_triangle = 0
    
    print("* To calculate the area of a Triangle, You Have to input Base and Height")
    print("* Surface Area = '(Base X Height)/2'")
    print("* d = Base (m)")
    print("* h = Height (m)\n")
    
    try:
        base_of_triangle = float(input("Enter The Base Of Triangle : "))
        height_of_triangle = float(input("Enter The Height Of Triangle : "))
        triangle = my_class.Triangle(base_of_triangle, height_of_triangle)
        area_of_triangle = triangle.area_calculation()
        
        return area_of_triangle
        
    
    except:
        print("---- Please Enter The Decimal Number ----")
        
    