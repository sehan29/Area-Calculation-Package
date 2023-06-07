import os
import Frontend.index_page
import Backend.Surface_Area.get_the_user_input
import Backend.Area.area
import Backend.Area.selecting_area_section
import Backend.Surface_Area.selecting_surface_area
import Backend.Combine_Object_Area.get_the_inputs_to_calculate_combile_area
import Backend.Combine_Object_Area.combine_shape_instructuin




def user_selection(value):
    if(value == 1):
        print("Area Calculation")
        os.system('cls')
        Frontend.index_page.obsacles()
        return_value = Backend.Area.area.secting_the_obstacle()
        Backend.Area.selecting_area_section.shape_filtering(return_value)

        
    elif(value == 2):
        print("Surface Area Calculation")
        os.system('cls')
        Frontend.index_page.surface_area_objects()
        user_value = Backend.Surface_Area.get_the_user_input.user_input()
        print(user_value)
        Backend.Surface_Area.selecting_surface_area.selecting_surface_area(user_value)
        
        
        
        
    elif(value == 3):
        
        obstacle_list = ['Circle','Rectanle','Triangle','Square']
        print("Combine Object Area Calculation")
        os.system('cls')
        area_of_one_obj = 0     
        current_objects = []
        mystring = ""
        
        """     print("How Many Iterms Do You Combine : ") """
        try:
            
            number_of_iterms = int(input("How Many Iterms Do You Combine : "))
            
            for i in range(0,number_of_iterms):
                
                Frontend.index_page.combination_shapes()
                first_user_input = Backend.Combine_Object_Area.get_the_inputs_to_calculate_combile_area.user_inputs()
                current_objects.append(first_user_input)
                area_of_one_obj += Backend.Combine_Object_Area.combine_shape_instructuin.shape_filtering(first_user_input)
                
            for i in range(0,number_of_iterms):
                
                
                mystring = mystring + obstacle_list[current_objects[i]]                
                
                if(i == number_of_iterms-1):
                    
                    break
                
                else:
                    
                    mystring += " and "
            
            print("The Area Of "+mystring+" = ",area_of_one_obj,'m\u00b2')
                    
            
        except:
            
            print("Please Enter The Decimal Value")
        
        

        
        

                  
        
    elif(value == 4):
        print("Exit")
    else:
        print("---- Invalid Number -----")