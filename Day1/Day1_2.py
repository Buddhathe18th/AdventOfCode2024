f=open("Day1_Input.txt", "r")
lines=f.readlines()
left,right=[],{}

for line in lines:
    values=line.split()
    left.append(values[0])
    if values[1] in right:
        right[values[1]]+=1
    else:
        right[values[1]]=1

print(right)

sum=0
for i in left:
    if i in right:
        sum+=right[i]*int(i)
print(sum)

#
# left=sorted(left)
# right=sorted(right)
# print(left)
# print(right)
#
# sum=0
# for i in range(1000):
#     sum=sum+abs(int(left[i])-int(right[i]))
# print(sum)