def rawInfoToReqInfo():
    with open("info.txt", "r",encoding="utf-8") as info:
        print('\n')
        for line in info:
            x = line.split()[1:6]
            print(x)

            f = open("infoMod.txt", "a")
            listToStr = ' '.join(map(str, x))
            f.write(f"{listToStr}\n")
            f.close()

def rawInfoToReqMarks():
    with open("marks.txt", "r",encoding="utf-8") as info:
        print('\n')
        for line in info:
            x = line.split()[1:-1]
            print(x)

            f = open("marksMod.txt", "a")
            listToStr = ' '.join(map(str, x))
            f.write(f"{listToStr}\n")
            f.close()