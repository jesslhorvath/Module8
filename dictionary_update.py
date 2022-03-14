"""
Program: dictionary_update.py
Author: Jessie Horvath
Last date modified: 03/06/2022

The purpose of this program is to allow a user to indicate how many
test scores they would like to input and enter them. The first 
function then creates a dictionary of scores. The second function
breaks the dictionary into two lists of keys and values and calculates
the average test score from the dictionary.
"""

def get_test_scores():
    scores_dict = dict()

    num_scores_str = input("How many test scores are you entering? ")
    try:
        num_scores = int(num_scores_str)
    except ValueError:
        print("That is not a number")

    for i in range(num_scores):
        score = input("Enter the test score: ")
        try:
            score = int(score)
        except ValueError:
            print("That is not a number")
        else:
            scores_dict.update({f'Score {i+1}':score})
    return scores_dict

def average_scores(dict):
    values_list = dict.values()
    sum = 0

    length = len(dict.keys())

    for value in values_list:
        int(value)
        sum += value

    average_calc = sum / length

    return average_calc

if __name__ == '__main__':
    the_dict = get_test_scores()

    print(average_scores(the_dict))
