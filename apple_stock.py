# The trade fee constant
FEE = .05
# get shares, old price and new price
share = float(input("How many shares do you want to buy: "))
old_price = float(input("What is the share price at time of purchase: "))
new_price = float(input("What is the share price at time of sale: "))

result = new_price*share - old_price*share - old_price*share*FEE

print("You purchased" + str(share) + " at a price of $" + \
      format(old_price, '.2f'))
print("You sold at a price of $" + format(new_price, '.2f'))

if (result >= 0):
    print("You gain $" + format(result, '.2f'))
else:
    print("You lost $"+ format(-result, '.2f'))
