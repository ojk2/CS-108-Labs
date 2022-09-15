"""CS 108 - Lab 3.0

this program will create new objects in
several data structure types.

@author: OWEN KOH (2635799)

THIS UPLOAD IS MY OWN
REINPLEMENTATION.

@date: Fall, 2022
"""

# as list so that you can add more scores later
score1 = int(input("score: "))
score2 = int(input("score: "))
scores = [score1, score2]

# as string to be salted, hashed later although
# it's not intending to take in real passwords
password = input("password: ")

# as tuple as coordinates cannot be changed
latitude = float(input("latitude: "))
longitude = float(input("longitude: "))
dorm = (latitude, longitude)

# as dictionary due to the state being associative with
#its capital.
state1 = input("state: ")
capital1 = input("capital: ")
state2 = input("state: ")
capital2 = input("capital: ")
state_capitals = {state1: capital1, state2: capital2}


#one-liners to get the inputs:
#scores = [int(input("score: ")), int(input("score"))]
#dorm = (float(input("latitude: ")), float(input("longitude: ")))
#state_capitals = {
#    input("state: "): input("capital: "),
#    input("state: "): input("capital: ")
#}