#code

#1st line is the number of test cases/arrays. min is 1, max 100
#2nd line is the size of the array. min is 1, max 100
#3rd line is the array
#4th line is the number to be found in the array.
#Each integer in the array is between 1 and 100

#Goal is to print the index of the element

#How would the input look for multiple arrays?
# l1-#cases l2,l3,l4 l5,l6,l7 etc

#Easiest solution would be to check each element starting from the first

def FindIndex(argArray, argElement):
    indexOfElement = -1
    for index in range(0, len(argArray)):
        try:
            int(argArray[index].strip())
        except ValueError:
            break
        if int(argArray[index].strip()) == argElement:
            indexOfElement = index
            break

    print(str(indexOfElement))


try:
    numcases = int(input())
except ValueError:
    numcases = 0
for line in range(0, numcases):
    validInput = True
    try:
        arraySize = int(input())
    except ValueError:
        pass
    # map applies int function to each section of the input string and puts that into an array
    array = input().split(" ")
    try:
        element = int(input())
    except ValueError:
        validInput = False
    if validInput == True:
        FindIndex(array, element)

#lessons learned
# don't take input for granted, make sure input is expected
# make sure to get rid of whitespace
# input() will only read one line at a time, not a large string seperated by \n
# each call of input() will read a new line