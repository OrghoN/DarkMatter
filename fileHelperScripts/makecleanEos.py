import sys
import pprint

if len(sys.argv)<2:
    print("Need filename as first Input")
else:
    fileList = open(sys.argv[1], 'r')
    List = []
    # preamble = "eosrm -r /store/user/oneogi/"
    preamble = "eosls /store/user/oneogi/"
    # subdirectories = ["/DIGI-RECO-1_e_v2","/DIGI-RECO-2_e_v2", "/GEN-SIM_e_v2"]
    for line in fileList:
        line=line.rstrip()
        print("echo \"", line, "\"" )
        print(preamble + line)
        # for subdirectory in subdirectories:
            # print(preamble + line + subdirectory)
