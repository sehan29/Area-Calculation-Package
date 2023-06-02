import Backend.Surface_Area.surface_area_instruction


def selecting_surface_area(entered_value):
    
    if(entered_value == 1):
        
        print("Circle")
        Backend.Surface_Area.surface_area_instruction.circle()
        
    
    elif(entered_value == 2):
        print("Rectanle")
        pass
    
    elif(entered_value == 3):
        print("Triangle")
        pass
    
    elif(entered_value == 4):
        print("Square")
        pass
    elif(entered_value == 5):
        print("Cylinder")
        pass
    
    else:
        print("--- Please Enter The Decimal Number ---")