f=open("Day11_Input.txt", "r")
line=f.readline()

stones=line.split(" ")
newStones=[]

for i in range(25):
    for stone in stones:
        if stone=="0":
            newStones.append("1")
        elif len(stone)%2==0:
            newStones.append(str(int(stone[0:len(stone)//2])))
            newStones.append(str(int(stone[len(stone)//2:])))
        else:
            newStones.append(str(int(stone)*2024))

    stones=newStones
    newStones=[]
    print(stones)

print(len(stones))