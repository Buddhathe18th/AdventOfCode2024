import re

f=open("Day4_Input.txt", "r")
lines=f.readlines()
count=0
for line in range(1,len(lines)-1):
    for letter in range(1,len(lines[line])-1):
        if lines[line][letter]=="A":
            diagonalLeftToRight=False
            diagonalRightToLeft=False
            if (lines[line-1][letter-1]=="M" and lines[line+1][letter+1]=="S") or (lines[line+1][letter+1]=="M" and lines[line-1][letter-1]=="S"):
                diagonalLeftToRight=True
            if (lines[line-1][letter+1]=="M" and lines[line+1][letter-1]=="S") or (lines[line-1][letter+1]=="S" and lines[line+1][letter-1]=="M"):
                diagonalRightToLeft=True
            if diagonalLeftToRight and diagonalRightToLeft:
                count+=1



print(count)