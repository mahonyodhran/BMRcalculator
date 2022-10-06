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


def get_gender():
    '''get user input for a gender
    '''
    while True:
        gender = str(input("Are you [m]ale or [f]emale? :")).lower()
        if gender == str("m") or gender == str("f"):
            return gender
        print("Please enter [m] or [f]")
