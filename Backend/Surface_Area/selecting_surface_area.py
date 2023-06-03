import Backend.Surface_Area.surface_area_instruction


def selecting_surface_area(entered_value):
    
    if(entered_value == 1):
        
        print("Circle")
        Backend.Surface_Area.surface_area_instruction.circle()
        
    
    elif(entered_value == 2):
        print("Rectanle")
        Backend.Surface_Area.surface_area_instruction.rectangle()
    
    elif(entered_value == 3):
        print("Triangle")
        
    
    elif(entered_value == 4):
        print("Square")
        Backend.Surface_Area.surface_area_instruction.instruction_cube()
        
    elif(entered_value == 5):
        print("Cylinder")
        Backend.Surface_Area.surface_area_instruction.cylinder()
        
    
    else:
        print("--- Please Enter The Decimal Number ---")