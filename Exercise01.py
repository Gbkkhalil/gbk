#practicepython.org
#Exercise 01: Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime
name = input("What's your name: ")
print("Hello,", name, "the lenght of your name is: ", len(name))
age = int(input("what's your age: "))
n_age = (100 - age)
date = datetime.datetime.now()
print("In ", date.year+n_age, "you will be 100 years old !")

