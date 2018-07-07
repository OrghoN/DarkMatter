import sys
import pprint
import re

if len(sys.argv)<2:
    print("Need filename as first Input")
else:
    log = open(sys.argv[1], 'r')
    tableKeys = ["idle", "failed", "finished", "done", "unsubmitted"]
    print("{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}".format("Mass Point",tableKeys[0],tableKeys[1],tableKeys[2],tableKeys[3],tableKeys[4]))
    print("====================================================================================================")
    statusPattern = r'(\d+).(\d+)% \( *(\d+).(\d+)\)'
    firstMass = True
    for line in log:
        line=line.rstrip()
        if line.find("CRAB project directory:") != -1:
            codex = re.search(r'crab_DM_Codex_(\d+)_(\d+)_(\d+)',line).group()[14:]
            if not firstMass:
                print ("{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}".format(codex,tableValues[0],tableValues[1],tableValues[2],tableValues[3],tableValues[4]))
            firstMass = False
            tableValues = ["","","","",""]

        for index, key in enumerate(tableKeys):
            if line.find(key) != -1:
                if re.search(statusPattern,line) is not None:
                    tableValues[index] = re.search(statusPattern,line).group()



        # if line.find(sys.argv[2]) != -1:
    #         # status = re.search(r'(\d+).(\d+)% \( *(\d+).(\d+)\)',line)
    #         status = re.search(statusPattern,line)
            # if status is None:
    #             continue
    #         print (codex + " | " + status.group())
