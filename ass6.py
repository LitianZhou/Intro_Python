# weekly assignment 6

# part 1: writing to a file

# open a file
def main():
    write_scores()
    print("A file named 'scores.txt' has been written!")
    read_scores()
    print("The file content is printed above.")

def write_scores():
    scores = open("scores.txt", 'w')
    while True:
        # write one record
        print("Please input the student info: ")
        _name = input("Name: ")
        _id = input("ID: ")
        _score = input("Score: ")
        
        scores.write("Name:\t"+_name+"\n")
        scores.write("ID:\t"+_id+"\n")
        scores.write("Score:\t"+_score+"\n")
        
        more_stu = input("More students? 'yes' or 'no': ").lower()
        if more_stu in ('no', 'not', 'n'):
            break
        
    scores.close()
    
def read_scores():
    # open the file by input name of the file
    try:
        file_name = input("Which file to open? ")
        scores = open(file_name, 'r')
    
        # read the first line:
        next_field = scores.readline()
        # read to the end
        while next_field != '':
            print(next_field.rstrip('\n'))
            print(scores.readline().rstrip('\n'))
            print(scores.readline())
            next_field = scores.readline()
        scores.close()
    except IOError:
        print("Can not find the file named ")
        print(file_name)
        print("Try again! Exitting")
    except ValueError:
        print("Number conversion error. Try again.")
main()