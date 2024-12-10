f=open("Day8_Input.txt", "r")
lines=f.readlines()

wavelengths={}
for i in range(len(lines)):
    for j in range(len(lines[0])-1):
        if lines[i][j]!=".":
            if lines[i][j] not in wavelengths:
                wavelengths[lines[i][j]]=[(i,j)]
            else:
                wavelengths[lines[i][j]].append((i,j))

print(wavelengths)

antiNodeBoard=[[False for i in range(len(lines[0])-1)] for i in range(len(lines))]

print(antiNodeBoard)

for key in wavelengths:
    for i in range(len(wavelengths[key])):
        for j in range(i+1,len(wavelengths[key])):
            wavelength=wavelengths[key]
            newVector=(wavelength[i][0]-wavelength[j][0],wavelength[i][1]-wavelength[j][1])
            anti1=(newVector[0]+wavelength[i][0],newVector[1]+wavelength[i][1])
            anti2=(wavelength[j][0]-newVector[0],wavelength[j][1]-newVector[1])

            if not (anti1[0]<0 or anti1[1]<0 or anti1[0]>=len(antiNodeBoard) or anti1[1]>=len(antiNodeBoard[0])):
                antiNodeBoard[anti1[0]][anti1[1]]=True
                print(anti1[0],anti1[1])
                print("1")
            if not (anti2[0]<0 or anti2[1]<0 or anti2[0]>=len(antiNodeBoard) or anti2[1]>=len(antiNodeBoard[0])):
                antiNodeBoard[anti2[0]][anti2[1]]=True
                print(anti2[0], anti2[1])
                print("2")

count=0

for i in antiNodeBoard:
    for j in i:
        if j:
            count+=1

print(count)
