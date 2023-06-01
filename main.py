import Frontend.index_page as x
import Backend.user_inputs as user
import Backend.selecting as selecting
import Backend.Area.area
import Backend.Area.selecting_area_section


x.first_interface()
x = user.get_user_input()
selecting.user_selection(x)
return_value = Backend.Area.area.secting_the_obstacle()
Backend.Area.selecting_area_section.shape_filtering(return_value)






