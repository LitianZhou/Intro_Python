color1 = input("Please input first color: ")
color2 = input("Please input second color: ")

if (color1=="red" and color2=="yellow") or (color1=="yellow" and color2=="red"):
    print("When you mix red and yellow, you get orange.")
elif (color1=="red" and color2=="blue") or (color1=="blue" and color2=="red"):
    print("When you mix red and blue, you get purple.")
elif (color1=="yellow" and color2=="blue") or (color1=="blue" and color2=="yellow"):
    print("When you mix blue and yellow, you get green.")
else:
    print("You didn't input two primary colors.")
