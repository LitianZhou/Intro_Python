# General requirements
# 1. The program will internally do the calculation for the users.
# 2. The program is friendly interactive with the end-users.
# 3. The program shall print out the results in an informative way.

# Specific requirement
# 1. The program will give users prompts of input expectation.
# 2. The program will store 5 ingredient names and their amounts.
# 3. The program will store serving size for the recipe and \
#    calculate how much of each ingredient the user need after \
#    user tells it how many people to feed.

# Greetings
print("Hello World! Let us make great recipe!\n")

#input the serving size of the recipe
serving_size = float(input("How many people does this recipe serve? "))

#input the each ingredients' name and needed amount
ingredient1 = input("The first ingredient name: ")
amount1 = float(input("The amount in gram: "))

ingredient2 = input("The second ingredient name: ")
amount2 = float(input("The amount in gram: "))

ingredient3 = input("The third ingredient name: ")
amount3 = float(input("The amount in gram: "))

ingredient4 = input("The forth ingredient name: ")
amount4 = float(input("The amount in gram: "))

ingredient5 = input("The fifth ingredient name: ")
amount5 = float(input("The amount in gram: "))

#input the people user is going to serve
serving_number = float(input("How many people are you going to serve today? \n"))

#calculate the ratio of amounts
RATIO = serving_number/serving_size

#print the ingredients and their needed amount
print("These are the ingredients and individual amounts you need: ")
print(format(ingredient1, '12') + format((amount1*RATIO), ',.2f')+ " grams")
print(format(ingredient2, '12') + format((amount2*RATIO), ',.2f')+ " grams")
print(format(ingredient3, '12') + format((amount3*RATIO), ',.2f')+ " grams")
print(format(ingredient4, '12') + format((amount4*RATIO), ',.2f')+ " grams")
print(format(ingredient5, '12') + format((amount5*RATIO), ',.2f')+ " grams")





