f=open("Day9_Input.txt", "r")
line=f.readline()

files=[]

id=0
file=True
for i in range(len(line)):
    if file:
        for i in range(int(line[i])):
            files.append(str(id))
        file=False
        id+=1
    else:
        for i in range(int(line[i])):
            files.append(".")
        file=True

print(files)


firstEmpty=0
while files[firstEmpty]!=".":
    firstEmpty+=1

for i in range(len(files)-1,-1,-1):
    if firstEmpty >= i:
        break

    if files[i]!=".":
        files[firstEmpty]=files[i]
        files[i]="."

        while files[firstEmpty] != ".":
            firstEmpty += 1

print(files)

for i in range(len(files)-1,-1,-1):
    if files[i]==".":
        files.pop(i)

print(files)


checksum=0
for i in range(len(files)):
    checksum+=i*int(files[i])

print(checksum)