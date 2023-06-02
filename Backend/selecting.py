import os
import Frontend.index_page
import Backend.Surface_Area.get_the_user_input
import Backend.Area.area
import Backend.Area.selecting_area_section
import Backend.Surface_Area.selecting_surface_area


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
        print("Combine Object Area Calculation")
    elif(value == 4):
        print("Exit")
    else:
        print("---- Invalid Number -----")