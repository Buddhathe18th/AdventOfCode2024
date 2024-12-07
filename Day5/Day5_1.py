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