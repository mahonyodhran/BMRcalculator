def mifflin_st_jeor(age, height, weight, gender):
    if(gender == 'M'):
        bmr = (10*weight)+(6.25*height)-(5*age) + 5
    else:
        bmr = (10*weight)+(6.25*height)-(5*age) - 161
    print('\nYour BMR is: {} calories'.format(int(bmr)))