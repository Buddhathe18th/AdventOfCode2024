import re

f=open("Day3_Input.txt", "r")


lines=f.readlines()
a=0
enable=True
for line in lines:
    sum=0
    matches=re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))",line)
    print(matches)

    for i in matches:
        if i[0][0]=="m" and enable:
            sum+=int(i[1])*int(i[2])
        elif i[0]=="do()":
            enable=True
        else:
            enable=False

    print(sum)
    a = a + sum
print(a)




#
#
#     for match in matches:
#         sum=sum+int(match[0])*int(match[1])
#
#
#     print(sum)
#     a=a+sum
#
# print(a)