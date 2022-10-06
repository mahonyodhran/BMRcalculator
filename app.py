from methods.equations import mifflin_st_jeor, tdee
from methods.inputs import get_float, tdee_info, get_gender
from user import User

age = get_float('age')
height = get_float('height')
weight = get_float('weight')
gender = get_gender()

new_user = User("Odhran", age, weight, height, gender)

bmr = mifflin_st_jeor(new_user.age, new_user.height, new_user.weight, new_user.gender)

print('\n*** TDEE ***')
#TO BE EXTRACTED#
tdee_result = input('Would you like to calculate your TDEE? [y/N]: ')
if tdee_result.lower() =='y':
    tdee(bmr) 
    info = input('\nWould you like more info on TDEE? [y/N]: ')
    if info.lower() =='y':
        tdee_info() 
#TO BE EXTRACTED#

print('Thanks for using the system, goodbye!')