# code

def findFactors(argArray, argProduct):
    # array is unsorted
    # simple checking each element if it is a factor would be O(n-1)^2
    # easier to put possibilites into a sorted array?
    answer = False
    if argProduct == 0:
        # search for 0
        for index in range(0, len(argArray)):
            try:
                element = int(argArray[index].strip())
            except ValueError:
                continue
            if element == 0:
                answer = True
    else:
        posFactors = []
        # narrow list of possibilities
        for index in range(0, len(argArray)):
            try:
                target = int(argArray[index].strip())
            except ValueError:
                continue
            if target == 0:
                continue
            elif argProduct % target == 0:
                posFactors.append(target)
        # search for factors
        for indexF in range(0, len(posFactors)):
            targetFactor = argProduct/posFactors[indexF]
            for indexP in range (0, len(posFactors)):
                if indexP is not indexF:
                    if posFactors[indexP] == targetFactor:
                        answer = True
                        break
            if answer is True:
                break
    if answer is False:
        print("No")
    else:
        print("Yes")


# handle input parsing
try:
    numcases = int(input().strip())
except ValueError:
    numcases = 0

for inputLine in range(0, numcases):
   # print("\n case: " + str(inputLine))

    targetinputs = input().split()
    # print(targetinputs)

    array = input().split()
    # print("size: " + str(len(array)))
    if (len(targetinputs)) != 2:
        # print("bad targets")
        continue

    #print(array)

    try:
        inputProduct = int(targetinputs[1].strip())
    except ValueError:
        print("No")
        continue
    if len(array) != 0:
        findFactors(array, inputProduct)

#For some reason Pycharm not showing complete output, but correct on Geek for Geeks site
# Python else if is elif
# Use mod is see if an integer is a factor of another integer