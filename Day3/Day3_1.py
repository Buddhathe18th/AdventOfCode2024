import re

f=open("Day3_Input.txt", "r")


lines=f.readlines()
a=0
for line in lines:
    sum=0

    matches=re.findall("mul\((\d+),(\d+)\)",line)
    for match in matches:
        sum=sum+int(match[0])*int(match[1])


    print(sum)
    a=a+sum

print(a)