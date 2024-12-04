f=open("Day2_Input.txt", "r")
lines=f.readlines()
counter=0
for line in lines:
    line=line.split()
    work = False
    for i in range(0,len(line)):

        lineDropOne=line.copy()
        lineDropOne.pop(i)
        print(lineDropOne)

        if int(lineDropOne[1]) - int(lineDropOne[0]) > 0:
            a = True
            for i in range(len(lineDropOne) - 1):
                if int(lineDropOne[i + 1]) - int(lineDropOne[i]) > 3 or int(lineDropOne[i + 1]) - int(
                        lineDropOne[i]) < 1:
                    a = False
                    break
            if a:
                work=True
        elif int(lineDropOne[1]) - int(lineDropOne[0]) < 0:
            a = True
            for i in range(len(lineDropOne) - 1):
                if int(lineDropOne[i + 1]) - int(lineDropOne[i]) < -3 or int(lineDropOne[i + 1]) - int(
                        lineDropOne[i]) > -1:
                    a = False
                    break
            if a:
                work = True

        if work:
            break
    if work:
        counter+=1





print(counter)