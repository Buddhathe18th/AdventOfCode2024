f=open("Day1_Input.txt", "r")
lines=f.readlines()
left,right=[],[]

for line in lines:
    values=line.split()
    left.append(values[0])
    right.append(values[1])


left=sorted(left)
right=sorted(right)
print(left)
print(right)

sum=0
for i in range(1000):
    sum=sum+abs(int(left[i])-int(right[i]))
print(sum)