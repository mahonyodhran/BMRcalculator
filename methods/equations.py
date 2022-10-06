"""module for any methods that do mathy work
"""


def mifflin_st_jeor(age, height, weight, gender):
    """calculate the bmr using this calculation [in time will pass User]"""
    if gender == "m":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    print(f"\nYour BMR is: {int(bmr)} calories")
    return bmr


def tdee(bmr):
    """get the tdees for the calculated bmr"""
    values = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extremely Active": 1.9,
    }

    for lifestyle, calorie_amount in values.items():
        print(
            f"Your TDEE for {lifestyle} lifestyle is: {int(bmr * calorie_amount)} calories"
        )
