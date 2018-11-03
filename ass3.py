FEVER_TEM = 98.6

#Part 1
print("This is the part one")
fever = False
temperature = float(input("Part1: Please type in your temperature in fahranheit: "))

if temperature > FEVER_TEM:
    fever = True
    print("skip school and see a doctor!")
print("Fever was set to {} because temperature was {}".format(fever, temperature))
print("_________________________________________________________________")

#Part 2
print("This is the part two")

fever = False
temperature = float(input("Part2: Please type in your temperature in fahranheit: "))

if temperature > FEVER_TEM:
    fever = True
    print("skip school and see a doctor!")
else:
    fever = False
    print("stop faking and head to class")

if fever:
    print("Fever was set to {} because temperature was above 98.6".format(fever))
else:
    print("Fever was set to {} because temperature was below 98.6".format(fever))
print("_________________________________________________________________")

#Part 3
print("This is the part three~")

a = int(input("Please input the first integer: "))
b = int(input("Please input the second integer: "))
c = int(input("Please input the third integer: "))

if a <= b and a <= c:
    print(a)
    if b <= c:
        print(b,c, sep='\n')
    else:
        print(c,b,sep='\n')
elif b <= a and b <= c:
    print(b)
    if a<=c:
        print(a,c,sep='\n')
    else:
        print(c,a,sep='\n')
elif c <= a and c <= b:
    print(c,sep='\n')
    if a <= b:
        print(a,b,sep='\n')
    else:
        print(b,a,sep='\n')
print("Surprise!")
