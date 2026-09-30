import os
import matplotlib.pyplot as plt

data_path = "/Users/kwoodakw/415 proj/CS415_PROJ1"

def readFile(n, secondary, folder="testSet"):
    path = os.path.join(data_path, folder, "data" + str(n) + secondary + ".txt")
    with open(path, "r") as file:
        return [int(line.strip()) for line in file]

    
def InsertionSort(list):
    numOfComparisons = 0

    for n in range(1, len(list)):
        curr = list[n]
        j = n - 1

        while j >= 0:
            numOfComparisons += 1

            if list[j] > curr:
                list[j + 1] = list[j]
                j -= 1
            else:
                break

        list[j + 1] = curr

    return list, numOfComparisons

def SelectionSort(list):
    numOfComparisons = 0 
    
    for i in range(len(list) - 1, 0, -1):
        biggestval = 0

        for j in range(1, i + 1):
            numOfComparisons += 1

            if list[j] > list[biggestval]:
                biggestval = j

        list[i], list[biggestval] = list[biggestval], list[i]

    return list, numOfComparisons

        

def fib(i, NumAdditions):
    if(i == 1):
        return 1, NumAdditions
    if(i == 0):
        return 0, NumAdditions
    
    fib1, NumAdditions = fib(i - 1, NumAdditions)
    fib2, NumAdditions  = fib(i - 2, NumAdditions)


    NumAdditions += 1 

    return fib1 + fib2 , NumAdditions

def euclids(m, n, numComp):
    if n == 0:
        return numComp
    
    numComp += 1 

    var = m % n

    return euclids(n, var, numComp)


def expo_dec_by_one(a, n, mult):
    if n == 0:
        return 1, mult
    
    mult += 1
    curr_val, mult = expo_dec_by_one(a, n-1, mult)
    return (a * curr_val), mult

def expo_dec_by_const(a, n, mult):
    if n == 0:
        return 1, mult
    
    elif n % 2 == 0:
        mult += 1
        curr_val, mult = expo_dec_by_const(a, n//2, mult)
        return (curr_val ** 2), mult
    
    else:
        mult += 1
        curr_val, mult = expo_dec_by_const(a, (n-1)//2, mult)
        return ((curr_val ** 2) * a), mult + 1


def expo_div_and_conq(a, n, mult):
    if n == 0:
        return 1, mult
    
    elif n % 2 == 0:
        mult += 1
        curr_val, mult = expo_div_and_conq(a, n//2, mult)
        curr_val2, mult = expo_div_and_conq(a, n//2, mult)
        return (curr_val * curr_val2), mult 
    
    else:
        mult += 1
        curr_val, mult = expo_div_and_conq(a, (n-1)//2, mult)
        curr_val2, mult = expo_div_and_conq(a, (n-1)//2, mult)
        return ((curr_val * curr_val2) * a), mult + 1


def dataTest(data):
    placeHolder, insertionData = InsertionSort(data.copy())
    placeHolder, selectionData = SelectionSort(data.copy())
    return insertionData, selectionData

def GetTestSizes():
        sizes = list(range(100,10000,1000))
        sizes.append(10000)
        return sizes

def userinput():
    i = int(input("What is your kth number you would like to compute "))

    numComp = 0

    FibNumber, NumAdditions = fib(i, 0)

    
    m, placeHolder = fib(i + 1, 0)
    n, placeHolder = fib(i, 0)

    modulo_div = euclids(m, n, numComp)


    print("kth fibonacci term is ", FibNumber)
    print("Num additions is ", NumAdditions)
    print("The number of modulo divisions is ", modulo_div)

    print()

    base = int(input("For exponentiation would would you like your base to be? "))
    exponent = int(input("What would you like your exponent to be? "))
    

    by_one, one_mult = expo_dec_by_one(base, exponent, 0)
    by_const, const_mult = expo_dec_by_const(base, exponent, 0)
    div_conq, conq_mult = expo_div_and_conq(base, exponent, 0)



    print("Decrease by one outputs", by_one)
    print("Decrease by a constant outputs", by_const)
    print("Divide and conquire outputs", div_conq)

    print()

    n = int(input("What size list would you like to sort (10 - 100, increment of 10)? "))
    data = readFile(n, "", "smallSet")

    sortedInsertion, insertionComparisons = InsertionSort(data.copy())
    sortedSelection, selectionComparisons = SelectionSort(data.copy())

    print("Insertion sort result: ", sortedInsertion)
    print("Insertion sort number of comparisons: ", insertionComparisons)
    print("Selection sort result: ", sortedSelection)
    print("Selection sort number of comparisons: ", selectionComparisons)  


def scatterplot():
    NumAdditions = 0
    numComp = 0

    kValues = []
    additionValues = []

    #Prints the number of additions when running the fibinocci sequence from ranges 0-40
    print("(k, A(k))")

    for i in range (0, 40, 5):
        NumAdditions = 0
        FibNumber, NumAdditions = fib(i, NumAdditions)

        kValues.append(i)
        additionValues.append(NumAdditions)
        
       # print("(", i, ", ", NumAdditions, ")")

    plt.scatter(kValues, additionValues)
    plt.title("fib sequence graph")
    plt.xlabel("k")
    plt.ylabel("number of additions")
    plt.show()

    #Prints the number of modulo divisions in the worst case from 0-40
    print()
    #print("(n, D(N))")

    nValues = []
    divisionValues = []

    for i in range (0, 40, 5):
        #could improve this given the time making use of values generated from task 1a
        NumAdditions = 0
        m, NumAdditions = fib(i + 1, NumAdditions)
        NumAdditions = 0
        n, NumAdditions = fib(i, NumAdditions)
        
        numComp = 0
        modulo_div = euclids(m, n, numComp)

        nValues.append(n)
        divisionValues.append(modulo_div)
        #print("(", n, ", ", modulo_div, ")")

    plt.figure()
    plt.scatter(nValues, divisionValues)
    plt.title("euclid graph")
    plt.xlabel("n values")
    plt.ylabel("number of div")
    plt.show()
    
    #Prints the number of multiplactions for decrease by one, decrease by constant, and divide and conquer for exponents
    print()
    print("(n, M(n))")
    
    base = 4
    #mult = 0

    xValues = []
    decByOneValues = []
    decByConstValues = []
    divAndConqValues = []
    
    for i in range (1, 40, 5):
        by_one, one_mult = expo_dec_by_one(base, i, 0)
        by_const, cont_mult = expo_dec_by_const(base, i, 0)
        div_conq, conq_mult = expo_div_and_conq(base, i, 0)

        xValues.append(i)
        decByOneValues.append(one_mult)
        decByConstValues.append(cont_mult)
        divAndConqValues.append(conq_mult)

        #print("Decrease by one: (", i, ", ", one_mult, ")")
        #print("Decrease by constant: (", i, ", ", cont_mult, ")")
        #print("Divide and conquer: (", i, ", ", conq_mult, ")")
        print()

    plt.figure()
    plt.scatter(xValues, decByOneValues, label = "Decrease by one")
    plt.scatter(xValues, decByConstValues, label = "Decrease by constant factor")
    plt.scatter(xValues, divAndConqValues, label = "Divide and conquer")
    plt.title("exponentiation graph")
    plt.xlabel("n")
    plt.ylabel("number of multiplications")
    plt.legend()
    plt.show()

    insertBestCase = []
    insertAverageCase = []
    insertWorstCase = []

    selectBestCase = []
    selectAverageCase = []
    selectWorstCase = []

    inputSize = GetTestSizes()

    #Prints the number of comparisons for insertion and selections sort
    #This grabs the sorted sets (best case)
    for i in range(100, 10000, 100):
        bestSet = readFile(i, "_sorted")
        averageSet = readFile(i, "")
        worstSet = readFile(i, "_rSorted")

        insertionComparisons, selectionComparisons = dataTest(bestSet)
        insertBestCase.append(insertionComparisons)
        selectBestCase.append(selectionComparisons)

        insertionComparisons, selectionComparisons = dataTest(averageSet)
        insertAverageCase.append(insertionComparisons)
        selectAverageCase.append(selectionComparisons)

        insertionComparisons, selectionComparisons = dataTest(worstSet)
        insertWorstCase.append(insertionComparisons)
        selectWorstCase.append(selectionComparisons)    


    plt.scatter(inputSize, insertBestCase, label="Insertion Sort")
    plt.scatter(inputSize, selectBestCase, label="Selection Sort")
    plt.title("Comparisons best Case")
    plt.xlabel("n")
    plt.ylabel("number of comparisons")
    plt.legend()
    plt.show()

    plt.scatter(inputSize, insertAverageCase, label="Insertion Sort")
    plt.scatter(inputSize, selectAverageCase, label="Selection Sort")
    plt.title("Comparisons average Case")
    plt.xlabel("n")
    plt.ylabel("number of comparisons")
    plt.legend()
    plt.show()

    plt.scatter(inputSize, insertWorstCase, label="Insertion Sort")
    plt.scatter(inputSize, selectWorstCase, label="Selection Sort")
    plt.title("Comparisons worst Case")
    plt.xlabel("n")
    plt.ylabel("number of comparisons")
    plt.legend()
    plt.show()

    
mode = int(input("Would you like Scatter Plot Mode (1) or User Testing Mode (2)? "))

if(mode == 1):
    scatterplot();
elif(mode == 2):
    userinput();

