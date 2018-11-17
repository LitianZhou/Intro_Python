# project2

def main():

    filename = "data.txt"

    data_file = readfile(filename)

    analyze(data_file) 

    data_file = readfile(filename, True)

    analyze(data_file)

    data_file = readfile(filename, False)

    analyze(data_file)
    
def readfile(filename, winner="all_team"):
    file = open(filename, 'r')
    entries = file.readlines()
    team_num = len(entries)//7
    team_dic = {}
    for i in range(team_num):
        if winner == "all_team":
            team_dic[entries[i*7]] = [float(entries[i*7+1]), float(entries[i*7+2]), 
                    float(entries[i*7+3]), float(entries[i*7+4]), float(entries[i*7+5])]
        else:
            if str(winner) == entries[i*7+6].rstrip():
               team_dic[entries[i*7]] = [float(entries[i*7+1]), float(entries[i*7+2]), 
                    float(entries[i*7+3]), float(entries[i*7+4]), float(entries[i*7+5])]
    return team_dic

def analyze(dic):
    min_list = []
    max_list = []
    avg_list = []
    for i in range(5):
        minimal = 1e3
        maximal = 0
        summation = 0
        for team in dic.keys():
            summation += dic[team][i]
            if dic[team][i] < minimal:
                minimal = dic[team][i]
            if dic[team][i] > maximal:
                maximal = dic[team][i]
        min_list.append(minimal)
        max_list.append(maximal)
        avg_list.append(format(summation/len(dic.keys()),'.2f'))

    print('\t' + 'PPG\t' + 'PAPG\t' + 'SHOTPG\t' + 'SHOTAPG\t' + 'PK')
    print('MIN\t' + str(min_list[0])+'\t'+ str(min_list[1])+'\t'+ 
            str(min_list[2])+'\t' + str(min_list[3])+'\t' + str(min_list[4]))
    print('MAX\t' + str(max_list[0])+'\t'+ str(max_list[1])+'\t'+ 
            str(max_list[2])+'\t' + str(max_list[3])+'\t' + str(max_list[4]))
    print('AVG\t' + str(avg_list[0])+'\t'+ str(avg_list[1])+'\t'+ 
            str(avg_list[2])+'\t' + str(avg_list[3])+'\t' + str(avg_list[4]))
    print("The analysis ends here, bye!\n")       

main()