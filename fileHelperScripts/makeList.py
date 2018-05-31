fileList = open('gridPackFileNameList.txt', 'r')
List = []

for line in fileList:
    lineList = line.split("_")
    massPoints = "_".join([lineList[1][2:],lineList[3], lineList[5]])
    List.append(massPoints)

print(List)
