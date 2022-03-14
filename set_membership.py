"""
Program: set_membership.py
Author: Jessie Horvath
Last date modified: 03/05/2022

The purpose of this program is to test whether a given value is contained 
within a given set. The in_set function returns a Boolean dependent on 
if the value is in the set while the print_message function prints a user
friendly message dependent on whether the value is in the set.
"""

def in_set(set, value):
    if value in set:
        return True
    else:
        return False

def print_message(boolean_result, test_value, test_set):
    if boolean_result == True:
        print(f"The value {test_value} is in the set {test_set}.")
    else:
        print(f"The value {test_value} is not in the set {test_set}.")

if __name__ == '__main__':
    string = ("cream sugar milk butter")
    test_set = set(string.split(" "))
    test_value1 = 'cream'
    test_value2 = 'eggs'

    boolean_result1 = in_set(test_set, test_value1)
    boolean_result2 = in_set(test_set, test_value2)

    print_message(boolean_result1, test_value1, test_set)
    print_message(boolean_result2, test_value2, test_set)
