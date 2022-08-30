def mifflin_st_jeor(age, height, weight, gender):
    if(gender == 'M'):
        bmr = (10*weight)+(6.25*height)-(5*age) + 5
    else:
        bmr = (10*weight)+(6.25*height)-(5*age) - 161
    print('\nYour BMR is: {} calories'.format(int(bmr)))
    return bmr

def tdee(bmr):
    values = {'Sedentary': 1.2,
              'Lightly Active' : 1.375,
              'Moderately Active' : 1.55,
              'Very Active' : 1.725,
              'Extremely Active' : 1.9}
    
    for x,y in values.items():
        print('Your TDEE for {} lifestyle is: {} calories'.format(x,int(bmr * y)))