import sys
import pprint
import re
from numpy import isclose
from numpy import sqrt

colorList = {
    "idle" : u"\x1B[31;33m\u2587\x1B[0m",
    "failed": u"\x1B[31;31m\u2587\x1B[0m",
    "running" : u"\x1B[31;94m\u2587\x1B[0m",
    "finished" : u"\x1B[31;32m\u2587\x1B[0m",
    "transferring" : u"\x1B[31;92m\u2587\x1B[0m",
}

def error_gen(actual, rounded):
    divisor = sqrt(1.0 if actual < 1.0 else actual)
    return abs(rounded - actual) ** 2 / divisor

def graphRound(percents):
    percents = list(map(lambda x: x/2, percents))
    if not isclose(sum(percents), 50):
        percents[4] += (50 - sum(percents))

    n = len(percents)
    rounded = [int(x) for x in percents]
    up_count = 50 - sum(rounded)
    errors = [(error_gen(percents[i], rounded[i] + 1) - error_gen(percents[i], rounded[i]), i) for i in range(n)]
    rank = sorted(errors)
    for i in range(up_count):
        rounded[rank[i][1]] += 1
    return rounded

def buildGraph(values):
    keys = ["idle", "failed", "running", "finished", "transferring"]

    values = list(map(lambda x: 0.0 if x=="" else float(re.search(r'(\d+).(\d+)',x).group()), values))
    values = graphRound(values)

    graph = ""

    for color, value in enumerate(values):
        for i in range(0, value):
            graph +=colorList[keys[color]]

    return graph

if len(sys.argv)<2:
    print("Need filename as first Input")
else:
    log = open(sys.argv[1], 'r')
    tableKeys = ["idle", "failed", "running", "finished", "transferring" , "done", "unsubmitted"]

    print((u"{:^4}\u2502"+8*u"{:^16}\u2502"+u"{:^50}").format("#","Mass Point",tableKeys[0],tableKeys[1],tableKeys[2],tableKeys[3],tableKeys[4],tableKeys[5],tableKeys[6],"graphical")).encode('utf-8')
    print((4*u"\u2550"+u"\u256A")+(8*(16*u"\u2550"+u"\u256A"))+(50*u"\u2550")).encode('utf-8')

    statusPattern = r'(\d+).(\d+)% \( *(\d+).(\d+)\)'

    massNumber = 0

    for line in log:
        line=line.rstrip()
        if line.find("CRAB project directory:") != -1:
            if massNumber != 0:
                print ((u"{:^4}\u2502"+8*u"{:^16}\u2502"+u"{:^50}").format(massNumber,codex,tableValues[0],tableValues[1],tableValues[2],tableValues[3],tableValues[4],tableValues[5],tableValues[6],buildGraph(tableValues[0:5]))).encode('utf-8')
            codex = re.search(r'crab_DM_Codex_(\d+)_(\d+)_(\d+)',line).group()[14:]
            massNumber += 1
            tableValues = ["","","","","","",""]

        for index, key in enumerate(tableKeys):
            if line.find(key) != -1:
                if re.search(statusPattern,line) is not None:
                    tableValues[index] = re.search(statusPattern,line).group()
    print ((u"{:^4}\u2502"+8*u"{:^16}\u2502"+u"{:^50}").format(massNumber,codex,tableValues[0],tableValues[1],tableValues[2],tableValues[3],tableValues[4],tableValues[5],tableValues[6],buildGraph(tableValues[0:5]))).encode('utf-8')
