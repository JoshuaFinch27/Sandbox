"""
Lecture 8 DTN

Given a dictionary like:

name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}

Write a function that takes 2 parameters:
 - a dictionary like this
 - an integer threshold age value

The function should return a list of names of the people who are older or equal to the threshold age.

e.g: whatever_you_call_it(name_to_age, 30)
        should return ["Jane", "Sven"]

"""

name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}


def main()
    """Main program, calls other function and prints output"""
    names = names_above_threshold(30)
    print(f"{names}")


def names_above_threshold(threshold):
    """Finds and returns the names of people who's age is over a threshold"""
    names = [name for name in name_to_age if name_to_age[name] >= threshold]
    return names


main()
