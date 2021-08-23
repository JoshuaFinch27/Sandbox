"""
Lecture 5 DTN

Write code for a function that takes 2 lists:
    - a list of names
    - a corresponding list of ages

That is, elements at the same list index represent the same person.
Should return the name of the oldest person in the list
Return the first name if multiple people have the same oldest age
"""


def main():
    """Lecture 5 demo on lists and functions"""
    names = ["Joshua", "Jack", "Joe"]
    ages = [18, 18, 25]
    print(determine_oldest(names, ages))


def determine_oldest(names, ages):
    """Determine the oldest name based on lists"""
    oldest_age = max(ages)
    index = ages.index(oldest_age)
    return names[index]


main()
