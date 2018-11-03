# Part 1
while True:
    RATE = 1.03
    while True:
        print("--------------------------------------")
        start_tuition = float(input("Please type in the starting tuition: "))
        if start_tuition <= 25000 and start_tuition >= 5000:
            break
        else:
            print("The starting tuition should be between 5,000 and 25,000 inclusive, please enter a valid value.")
    tuition = start_tuition
    year = "year"
    for i in range(1,6):
        tuition = tuition*RATE
        print("In " + str(i) + " " + year + ", the tuition will be $" + format(tuition, ',.2f') + ".")
        year = "years"
    foo = input("To calculate with other start tuition, type *yes* to continue, otherwise the program ends: ")
    if(foo != "yes"):
        break


# Part 2
print("\n_____________Part 2_______________")
while True:
    print("-----------------------------------------")
    rate = 1 + float(input("Please input the increment rate per year (enter as decimals): "))

#input start_tuition and validation check
    while True:
        start_tuition = float(input("Please type in the starting tuition: "))
        if start_tuition <= 25000 and start_tuition >= 5000:
            break
        else:
            print("ERROR: Starting tuition should be between 5,000 and 25,000 inclusive!")

#input first year + validation check
    while True:
        try:
            first_year = int(input("Please enter the first year you are interested: "))
        except ValueError:
            print("ERROR: Please input an integer!")
            continue
        else:
            if first_year < 1:
                print("ERROR: Please input a integer at least 1")
            else:
                break
#input last year + validation check
    while True:
            try:
                last_year = int(input("Please enter the last year you are interested: "))
            except ValueError:
                print("ERROR: Please input an integer!")
                continue
            else:
                if last_year < first_year:
                    print("ERROR: Please input a integer greater than first year")
                else:
                    break

# calculate and print
    tuition = start_tuition
    year = "year"
    for i in range(1, last_year+1):
        tuition = tuition*rate
        if i >= first_year:
            print("In " + str(i) + " " + year + ", the tuition will be $" + format(tuition, ',.2f') + ".")
        year = "years"
        
    foo = input("To calculate with other tuition and rate, type *yes* to continue, otherwise the program ends: ")
    if(foo != "yes"):
        break

