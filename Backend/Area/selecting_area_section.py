import os
import Backend.Combine_Object_Area.instruction_of_shapes



def shape_filtering(shape_number):
    if(shape_number == 1):
        
        os.system('cls')
        print("\033[1m" + "\t\tCircle" + "\033[0m")
        
        print("Circle")
     
             
    elif(shape_number == 2):
        
        os.system('cls')
        print("\033[1m" + "\t\tRectangle" + "\033[0m")
        
        print("Rectangle")
        
              
    elif(shape_number == 3):
        
        os.system('cls')
        print("\033[1m" + "\t\tTriangle" + "\033[0m")
        
        print("Triangle")
         
        
    elif(shape_number == 4):
       
        os.system('cls') 
        print("\033[1m" + "\t\tSquare" + "\033[0m")

        
        print("Square")
       
        
    else:
        
        os.system('cls')
        print("\t\tInvalid Number")