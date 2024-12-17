f=open("Day11_Input.txt", "r")
line=f.readline()

stones=line.split(" ")
stoneMatching={}
newStones=[]



for i in range(75):
    for stone in stones:

        if stone in stoneMatching:
            for s in stoneMatching[stone]:
                newStones.append(s)
        else:
            if stone=="0":
                stoneMatching[stone]=["1"]
                newStones.append("1")
            elif len(stone)%2==0:
                stoneMatching[stone] = [str(int(stone[0:len(stone)//2])),str(int(stone[len(stone)//2:]))]
                newStones.append(str(int(stone[0:len(stone)//2])))
                newStones.append(str(int(stone[len(stone)//2:])))
            else:
                stoneMatching[stone] = [str(int(stone)*2024)]
                newStones.append(str(int(stone)*2024))

    stones=newStones
    newStones=[]
    print(i)

print(len(stones))