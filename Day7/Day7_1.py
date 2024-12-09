f=open("Day7_Input.txt", "r")
lines=f.readlines()

def createOps(addedLength,results=[""]):
    if addedLength==0:
        return results

    newResults=[]
    for i in results:
        newResults.append(i+"+")
        newResults.append(i+"*")

    return createOps(addedLength-1,newResults)


sum=0
a=1

for line in lines:
    total=int(line.split(":")[0])
    numbers=list(map(int,line.split(":")[1].split(" ")[1:]))

    possibleOps=createOps(len(numbers)-1)


    for operation in possibleOps:
        val = numbers[0]
        for i in range(len(operation)):
            val=eval(str(val)+operation[i]+str(numbers[i+1]))
        if val==total:
            sum+=total
            break
    print(a)
    a+=1


print(sum)


