f=open("Day2_Input.txt", "r")
lines=f.readlines()
counter=0
for line in lines:
    line=line.split()
    if int(line[1])-int(line[0])>0:
        a=True
        for i in range(len(line)-1):
            if int(line[i+1])-int(line[i])>3 or int(line[i+1])-int(line[i])<1:
                a=False
                break
        if a:
            counter+=1
    elif int(line[1])-int(line[0])<0:
        a = True
        for i in range(len(line)-1):
            if int(line[i + 1]) - int(line[i]) <-3 or int(line[i + 1]) - int(line[i]) >-1:
                a = False
                break
        if a:
            counter += 1

print(counter)