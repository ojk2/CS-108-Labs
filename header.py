from sys import argv

script, targetFile = argv

openFile = open(targetFile).read()


print("Now enter a short description for the program.")

while True:
  input()
  
