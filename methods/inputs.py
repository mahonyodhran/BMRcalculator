'''module for any input required methods
'''


def get_float(value):
    '''get user input for a float amount
    '''
    while True:
        try:
            return float(input(f"Please enter your {value}: "))
        except ValueError:
            print(f"Your {value} should be a number!")


def tdee_info():
    '''print out tdee information
    '''
    print(
        "\n1: Sedentary\
            \n2: Lightly Active [1-3 times per week]\
            \n3: Moderately Active [3-5 times per week]\
            \n4: Very Active [6-7 times per week]\
            \n5: Extremely Active [2x per day / Athlete etc.]"
    )


def get_gender():
    '''get user input for a gender
    '''
    while True:
        gender = str(input("Are you [m]ale or [f]emale? :")).lower()
        if gender == str("m") or gender == str("f"):
            return gender
        print("Please enter [m] or [f]")
