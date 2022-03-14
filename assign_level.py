"""
Program: assign_level.py
Author: Jessie Horvath
Last date modified: 03/06/2022

The purpose of this program is to use a dictionary in a case
statement-like manner. The user enters the level of interest 
as a function parameter. The function searches the defined dictionary
for the key and returns the paired value.
"""

def switch_level(level):
    level = level.upper()
    level_dict = dict({'N':50, 'B':150, 'E':300, 'A':500})

    points = level_dict.get(level, "Not Found!")

    return points

if __name__ == '__main__':
    print(switch_level('N'))
    print(switch_level('B'))
    print(switch_level('E'))
    print(switch_level('A'))

    print(switch_level('Q'))
