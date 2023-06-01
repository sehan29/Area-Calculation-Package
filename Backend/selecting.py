import os
import Frontend.index_page



def user_selection(value):
    if(value == 1):
        print("Area Calculation")
        os.system('cls')
        Frontend.index_page.obsacles()
    elif(value == 2):
        print("Surface Area Calculation")
    elif(value == 3):
        print("Combine Object Area Calculation")
    elif(value == 4):
        print("Exit")
    else:
        print("---- Invalid Number -----")