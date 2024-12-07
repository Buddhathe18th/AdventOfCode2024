f=open("Day5_Input.txt", "r")
lines=f.readlines()

rules={}

for i in range(1176):
    rule=lines[i].split("|")



    if int(rule[0]) not in rules:
        rules[int(rule[0])]=[int(rule[1])]
    else:
        rules[int(rule[0])].append(int(rule[1]))

sum=0

for i in range(1177,len(lines)):
    line=lines[i].split(",")
    print(line)
    correct=True
    for first in range(len(line)):
        for second in range(first+1,len(line)):
            if int(line[second]) in rules:
                if int(line[first]) in rules[int(line[second])]:
                    correct=False


    if correct:
        sum+=int(line[(int(len(line)/2))])
        print("yay")

print(sum)



#
# count=0
# for line in range(len(lines)):
#     for letter in range(len(lines[line])):
#         if lines[line][letter]=="X":
#             if (letter+3 < len(lines[line])):
#                 if lines[line][letter]+lines[line][letter+1]+lines[line][letter+2]+lines[line][letter+3]=="XMAS":
#                     count=count+1
#
#             if (letter-3 >= 0):
#                 if lines[line][letter-3]+lines[line][letter-2]+lines[line][letter-1]+lines[line][letter]=="SAMX":
#                     count=count+1
#
#             if (line+3 < len(lines)):
#                 if lines[line][letter]+lines[line+1][letter]+lines[line+2][letter]+lines[line+3][letter]=="XMAS":
#                     count=count+1
#
#             if (line-3 >= 0):
#                 if lines[line-3][letter]+lines[line-2][letter]+lines[line-1][letter]+lines[line][letter]=="SAMX":
#                     count=count+1
#
#             if (line+3 < len(lines) and letter+3 < len(lines[line])):
#                 if lines[line][letter]+lines[line+1][letter+1]+lines[line+2][letter+2]+lines[line+3][letter+3]=="XMAS":
#                     count=count+1
#
#             if (line-3 >= 0 and letter-3 >= 0):
#                 if lines[line-3][letter-3]+lines[line-2][letter-2]+lines[line-1][letter-1]+lines[line][letter]=="SAMX":
#                     count=count+1
#
#             if (line+3 < len(lines) and letter-3 >= 0):
#                 if lines[line][letter]+lines[line+1][letter-1]+lines[line+2][letter-2]+lines[line+3][letter-3]=="XMAS":
#                     count=count+1
#
#             if (line-3 >= 0 and letter+3 < len(lines[line])):
#                 if lines[line-3][letter+3]+lines[line-2][letter+2]+lines[line-1][letter+1]+lines[line][letter]=="SAMX":
#                     count=count+1
#
#
# print(count)