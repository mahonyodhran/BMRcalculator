def get_float(value):
    while True:
        try:
            return float(input('Please enter your {}: '.format(value)))
        except ValueError:
            print("Your {} should be a number!".format(value))

def get_char(value):
    answer = input('Please enter your {}: '.format(value))
    if answer.lower() =='y':
        return True
    else:
        return False

def tdee_info():
            print('\n1: Sedentary\
            \n2: Lightly Active [1-3 times per week]\
            \n3: Moderately Active [3-5 times per week]\
            \n4: Very Active [6-7 times per week]\
            \n5: Extremely Active [2x per day / Athlete etc.]')