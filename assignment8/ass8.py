# Assignment 8

# part 1

letter_dic = {'A':2, 'B':2, 'C':2,
              'D':3, 'E':3, 'F':3,
              'G':4, 'H':4, 'I':4,
              'J':5, 'K':5, 'L':5,
              'M':6, 'N':6, 'O':6,
              'P':7, 'Q':7, 'R':7, 'S':7,
              'T':8, 'U':8, 'V':8,
              'W':9, 'X':9, 'Y':9, 'Z':9
            }
number_enter = input("Enter a 10-character telephone number in XXX-XXX-XXXX: ").upper()
number_digit = ''

for char in number_enter:
    if char in letter_dic.keys():
        number_digit += str(letter_dic[char])
    else:
        number_digit += char
print("The translated number is: " + number_digit)

# part 2

print("This is the part II")
read_file = open("phonebook.in", 'r')
buffer_list = read_file.readlines()
read_file.close()

contact_dic = {}
contact_num = len(buffer_list)//2
for i in range(contact_num):
    name = buffer_list[2*i].rstrip('\n')
    email = buffer_list[2*i+1].rstrip('\n')
    contact_dic[name] = email 

def main():
    option = 0
    while option != 5:
        print("-----Manu-----")
        print("1) look up an email address")
        print("2) add a new name and email address")
        print("3) change an email address")
        print("4) delete a name and email address")
        print("5) save address book and exit")

        option = int(input("please enter the number above: "))
        if option == 1:
            lookup()
        elif option == 2:
            add()
        elif option == 3:
            edit()
        elif option == 4:
            delete()
        elif option == 5:
            save()
        elif option == 0:
            break
        else:
            print("invalid input. Enter again")
    print("exiting. Goodbye Moonman!")

def lookup():
    name = input("Enter a name: ")
    if name in contact_dic.keys():
        print(contact_dic[name])
    
    else:
        print("Sorry, no contact exists under that name.")
    

def add():
    name = input("Enter a name: ")
    if name in contact_dic.keys():
        print("The name exists! Keep adding will overwrite: ")
        print(name + " " + contact_dic[name])
        overwrite = input("Y for overwrite, otherwise skip adding").upper()
        if overwrite:
            email = input("Enter an email: ")
            contact_dic[name] = email
            print("Add complete.")
        else:
            print("Keep the original.")
    
    else:
        email = input("Enter an email: ")
        contact_dic[name] = email
        print("Add complete.")

def edit():
    name = input("Enter a name: ")
    if name in contact_dic.keys():
        email = input("Enter the new email: ")
        contact_dic[name] = email
        print("Edit complete.")
    else:
        print("Sorry, no contact exists under that name to edit.")

def delete():
    name = input("Enter a name: ")
    if name in contact_dic.keys():
        del contact_dic[name]
        print("Delete complete.")
    else:
        print("Sorry, no contact exists under that name to delete.")

def save():
    write_file = open("phonebook.out", 'w')
    sorted_name = sorted(contact_dic)
    for key in sorted_name:
        write_file.writelines(key + '\n')
        write_file.writelines(contact_dic[key] + '\n')
    print("Saving complete.")
    write_file.close()
    

main()