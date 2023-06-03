import Backend.Area.obstacle_class as surface_method

def circle():
    
    
    radius = 0
    print("* To calculate Surface area of a circle, You Have to input Radius of Circle")
    print("* Area = π * r^2")
    print("* r = Radius (m)\n")
    
    try:
        
        radius_of_circle = float(input("Enter The Radius Of Circle : "))
        surface_circle = surface_method.Circle(radius_of_circle)
        surface_area = surface_circle.surface_area()
        print("-------------------------------------")
        print("The Area Of The Circle is ",surface_area,'m\u00b2')
        
    except:
        
        print("---- Please Enter The Decimal Number ----")
    
    

def cylinder():
    
    radius_of_circle = 0
    height_of_cycilder = 0
    print("* To calculate Surface area of a Cylinder, You Have to input Radius of Cylinder and Height")
    print("* Surface Area = 2πr^2 + 2πrh")
    print("* r = Radius (m)")
    print("* h = Height (m)\n")
    
    
    try:
        radius_of_cylinder = float(input("Enter The Radius Of Cylinder : "))
        height_of_cycilder = float(input("Enter The Heght Of Cylinder : "))
        surface_area_cylinder = surface_method.Cylinder(radius_of_cylinder, height_of_cycilder)
        area = surface_area_cylinder.surace_area()
        print("-------------------------------------")
        print("The Area Of The Circle is ",area,'m\u00b2')
    
    except:
        print("---- Pleace Enter The Decimal Number ----")
    
    

def rectangle():
    
    
    print("=---------------=")
    print("=               =")
    print("=               =")
    print("=               =")
    print("=---------------=\n")
    print("* To calculate Surface Area of a Rectangle, You Have to input Width , Height , Depth")
    print("* Surface Area = Rectangle ")
    print("* w = Width (m)")
    print("* h = Height (m)\n")
    
    
    try:
        
        width_of_rectangle = float(input("Enter The Width of Rectangle : "))
        height_of_rectangle = float(input("Enter The Heght Of Rectangle : "))
        rectangle_obj = surface_method.Rectangle(width_of_rectangle, height_of_rectangle)
        area_of_rectangle = rectangle_obj.surface_area()
        area_of_rectangle = round(area_of_rectangle,2)
        print("-------------------------------------")
        print("The Area Of The Rectanglr is ",area_of_rectangle,'m\u00b2')
    
    except:
        print("---- Please Enter The Decimal Number ----")
    
def instruction_cube():
    
    
    print("* To calculate surface area of a Cube, You Have to input Base and Height")
    print("* Surface Area = '(Width X Height) X 6'")
    print("* w = Width (m)")
    print("* h = Height (m)\n")
    
