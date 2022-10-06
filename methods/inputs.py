def get_float(value):
    while True:
        try:
            return float(input('Please enter your {}: '.format(value)))
        except ValueError:
            print("Your {} should be a number!".format(value))


def tdee_info():
            print('\n1: Sedentary\
            \n2: Lightly Active [1-3 times per week]\
            \n3: Moderately Active [3-5 times per week]\
            \n4: Very Active [6-7 times per week]\
            \n5: Extremely Active [2x per day / Athlete etc.]')
            
def get_gender():
    while True:
        gender = str(input("Are you [m]ale or [f]emale? :")).lower()
        if gender == str('m') or gender == str('f'):
            return gender
        else:
            print("Please enter [m] or [f]")
