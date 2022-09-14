"""CS 108 - Lab 3.2

This program will create a new dictionary and add several
entries. Then it will edit it with the instructions given:
1. Update Sally's value to be 13.
2. Delete the Tom-10 key-value pair.

@author: OWEN KOH (2635799)
@date: Fall, 2022
"""

# Put your solution code here, replacing this line.
score_dict = {"Joe": 10, "Tom": 23, "Barb": 13,
"Sue": 19, "Sally": 12
}

# use [brackets] to indicate the index for a key's value
print(score_dict["Barb"])

# update the key's value
score_dict["Sally"] = 13

# delete the tom-key-value pair entry from dictionary
del score_dict["Tom"]

print(score_dict)