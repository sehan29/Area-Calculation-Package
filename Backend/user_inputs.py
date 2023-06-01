def get_user_input():
    
    
    try:
        user_input_value = int(input("Enter Selected Number : "))
        return user_input_value
    
    except:
        print("Please Enter Decimal Number")
        get_user_input()
