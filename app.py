from equations import mifflin_st_jeor
from inputs import getFloat, getChar

age = getFloat('age')
height = getFloat('height')
weight = getFloat('weight')
gender = getChar()

mifflin_st_jeor(age, height, weight, gender)