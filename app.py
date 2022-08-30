from methods.equations import mifflin_st_jeor, tdee
from methods.inputs import get_float, get_char, tdee_info

age = get_float('age')
height = get_float('height')
weight = get_float('weight')
gender = get_char()

bmr = mifflin_st_jeor(age, height, weight, gender)
tdee(bmr)
info = input('Would you like more info on TDEE? [y/N]')
if info.lower() =='y':
    tdee_info() 
print('Thanks for using, goodbye!')