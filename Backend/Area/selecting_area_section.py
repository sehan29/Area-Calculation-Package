import os
import Backend.Area.shape_instruction as shape_ins



def shape_filtering(shape_number):
    if(shape_number == 1):
        
        os.system('cls')
        print("\033[1m" + "\t\tCircle" + "\033[0m")
        shape_ins.circle_instruction()
             
    elif(shape_number == 2):
        
        os.system('cls')
        print("\033[1m" + "\t\tRectangle" + "\033[0m")
        shape_ins.rectangle()
              
    elif(shape_number == 3):
        
        os.system('cls')
        print("\033[1m" + "\t\tTriangle" + "\033[0m")
        shape_ins.instruction_triangle()
        
    elif(shape_number == 4):
       
        os.system('cls') 
        print("\033[1m" + "\t\tSquare" + "\033[0m")
        shape_ins.instruction_square()
        
    elif(shape_number == 5):
        
        os.system('cls')
        print("\033[1m" + "\t\tCylinder" + "\033[0m")
        shape_ins.cylinder()
    else:
        
        os.system('cls')
        print("\t\tInvalid Number")