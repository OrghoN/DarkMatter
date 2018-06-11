import sys

if len(sys.argv)<2:
    print("Need filename as first Input")
else:
    fileList = open(sys.argv[1], 'r')
    List = []
    for line in fileList:
        line=line.rstrip()
        lineList = line.split("/")[1].split("_")
        massPoints = "_".join([lineList[2],lineList[3], lineList[4]])
        List.append([massPoints,line])
    print(List)
