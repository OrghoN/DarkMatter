import pprint
import sys

if len(sys.argv)<2:
    print("Need filename as first Input")
else:
    fileList = open(sys.argv[1], 'r')
    List = []

    for line in fileList:
        lineList = line.split("_")
        massPoints = "_".join([lineList[1][2:],lineList[3], lineList[5]])
        List.append(massPoints)

    pprint.pprint(List)
