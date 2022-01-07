import json
from operator import attrgetter

def rawInfoToReqInfo():
    with open("info.txt", "r",encoding="utf-8") as info:
        # print('\n')
        for line in info:
            x = line.split()[1:6]
            # print(x)

            f = open("infoMod.txt", "a")
            listToStr = ' '.join(map(str, x))
            f.write(f"{listToStr}\n")
            f.close()

def rawInfoToReqMarks():
    with open("marks.txt", "r",encoding="utf-8") as info:
        # print('\n')
        for line in info:
            x = line.split()[1:-1]
            # print(x)

            f = open("marksMod.txt", "a")
            listToStr = ' '.join(map(str, x))
            f.write(f"{listToStr}\n")
            f.close()

def matchAndCombine():
    infoMap = {}
    marksMap = {}
    resultMap = {}
    sortedMap = {}
    finalMap = {}
    with open("infoMod.txt", "r",encoding="utf-8") as infos:
        infoCount = 0
        for info in infos:
            infoCount += 1
            infoMap[infoCount] = info.split()
    with open("marksMod.txt", "r",encoding="utf-8") as marks:
        marksCount = 0
        for mark in marks:
            marksCount += 1
            marksMap[marksCount] = mark.split()
    matches = 0
    for infoKey in infoMap:
        x = infoMap[infoKey]
        for markKey in marksMap:
            y = marksMap[markKey]
            if (x[0]==y[0]):
                matches += 1
                try:
                    resultMap[matches] = x + [float(y[-1])]
                except:
                    pass

    for result in resultMap:
        sortedMap = sorted(resultMap, key=lambda x : resultMap[x][-1],reverse=True)

    for result in sortedMap:
        finalMap[result] = resultMap[result]
        # print(json.dumps(finalMap,indent=4))
        f = open("Civil_20-24_2ndSem_Result_Rankwise.txt", "a")
        listToStr = ' '.join(map(str, finalMap[result]))
        f.write(f"{listToStr}\n")
        f.close()


rawInfoToReqInfo()
rawInfoToReqMarks()
matchAndCombine()

# print(sorted(theList))