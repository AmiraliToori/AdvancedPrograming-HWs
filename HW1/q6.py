# 6. Restaurant Selector
# You have a group of friends coming to visit for your high school reunion, and you want
# to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary
# restrictions, but your restaurant choices are as follows:

# Joe’s Gourmet Burgers—     Vegetarian: No, Vegan: No, Gluten-Free: No
# Main Street Pizza Company— Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# Corner Café—               Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Mama’s Fine Italian—       Vegetarian: Yes, Vegan: No, Gluten-Free: No
# The Chef’s Kitchen—        Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

# Write a program that asks whether any members of your party are vegetarian, vegan, or
# gluten-free, to which then displays only the restaurants to which you may take the group.
# Here is an example of the program’s output:

# Is anyone in your party a vegetarian? yes Enter
# Is anyone in your party a vegan? no Enter
# Is anyone in your party gluten-free? yes Enter

# Here are your restaurant choices:
#  Main Street Pizza Company
#  Corner Cafe
#  The Chef's Kitchen

# Here is another example of the program’s output:
# Is anyone in your party a vegetarian? yes Enter
# Is anyone in your party a vegan? yes Enter
# Is anyone in your party gluten-free? yes Enter

#  Here are your restaurant choices:
#  Corner Cafe
#  The Chef's Kitchen


def comparison(diet, restaurant):
    for i in range(len(diet)):
        if (diet[i] == "yes"):
            if (restaurant[i + 1] == "no"):
                return 0
    return restaurant[0]


vegeterian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten_free = input("Is anyone in your party gluten-free? ")

friends_diet = [vegeterian, vegan, gluten_free]


restaurant = [["Joe’s Gourmet Burgers", "no", "no", "no"], ["Main Street Pizza Company", "yes", "no", "yes"],
              ["Corner Café", "yes", "yes", "yes"], ["Mama’s Fine Italian", "yes", "no", "no"], ["The Chef’s Kitchen", "yes", "yes", "yes"]]


print("Here are your restaurant choices: ")
for i in range(len(restaurant)):
    result = comparison(friends_diet, restaurant[i])
    if (result != 0):
        print(result)
