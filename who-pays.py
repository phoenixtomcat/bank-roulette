import random
#importing the random module to create a random number for us

#get the names of the persons in the group
print("Please enter the names of the persons in your group")
name1 = input("Person 1: ")
name2 = input("Person 2: ")
name3 = input("Person 3: ")
name4 = input("Person 4: ")
name5 = input("Person 5: ")
# Put the names in a list
names = [name1, name2, name3, name4, name5]

#randomly select a person's name from the list
random_item = len(names)
# 5 items but starts count at 0 and the last person is index 5 but (5-1=4th index, last place)
random_people = random.randint(0, random_item - 1)
print(names[random_people] + " is going to buy the meal today!")