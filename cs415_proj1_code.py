import matplotlib.pyplot as plt

def readFile(n, secondary):
    with open("data/testSet/data" + str(n) + secondary + ".txt", "r") as file:
        return [line.strip() for line in file]
    
def InsertionSort(list):
    for n in range(1, len(list)):
        curr = list[n]

        while list[n] < list[n-1]:
            list[n], list[n-1] = list[n-1], list[n]

def SelectionSort(list):
    biggestval = list[0]

    for n in list:
        if n > biggestval:
            biggestval = n

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
        return ((curr_val ** 2) * a), mult


def expo_div_and_conq(a, n, mult):
    if n == 0:
        return 1, mult
    
    elif n % 2 == 0:
        mult += 1
        curr_val, mult = expo_div_and_conq(a, n//2, mult)
        curr_val2, mult = expo_div_and_conq(a, n//2, mult)
        return ((curr_val * curr_val2) * a), mult + 1
    
    else:
        mult += 1
        curr_val, mult = expo_dec_by_const(a, (n-1)//2, mult)
        curr_val2, mult = expo_dec_by_const(a, (n-1)//2, mult)
        return ((curr_val * curr_val2) * a), mult


def userinput():
    i = int(input("What is your kth number you would like to compute "))

    NumAdditions = 0
    numComp = 0

    FibNumber, NumAdditions = fib(i, NumAdditions)

    NumAdditions = 0
    m, NumAdditions = fib(i + 1, NumAdditions)

    n, NumAdditions = fib(i, NumAdditions)

    modulo_div = euclids(m, n, numComp)


    print("kth fibonacci term is ", FibNumber)
    print("Num additions is ", NumAdditions)
    print("The number of modulo divisions is ", modulo_div)

    print()

    base = int(input("For exponentiation would would you like your base to be? "))
    exponent = int(input("What would you like your exponent to be? "))
    mult = 0

    by_one, mult = expo_dec_by_one(base, exponent, mult)
    by_const, mult = expo_dec_by_const(base, exponent, mult)
    div_conq, mult = expo_div_and_conq(base, exponent, mult)



    print("Decrease by one outputs", by_one)
    print("Decrease by a constant outputs", by_const)
    print("Divide and conquire outputs", div_conq)


    

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
    mult = 0

    for i in range (1, 40, 5):

        xValues = []
        decByOneValues = []
        decByConstValues = []
        divAndConqValues = []

        by_one, one_mult = expo_dec_by_one(base, i, mult)
        by_const, cont_mult = expo_dec_by_const(base, i, mult)
        div_conq, conq_mult = expo_div_and_conq(base, i, mult)

        xValues.append(i)
        decByOneValues.append(one_mult)
        decByConstValues.append(cont_mult)
        divAndConqValues.append(conq_mult)

        #print("Decrease by one: (", i, ", ", one_mult, ")")
        #print("Decrease by constant: (", i, ", ", cont_mult, ")")
        #print("Divide and conquer: (", i, ", ", conq_mult, ")")
        print()

    plt.figure()
    plt.scatter(xValues, decByOneValues)
    plt.scatter(xValues, decByConstValues)
    plt.scatter(xValues, divAndConqValues)
    plt.xlabel("number of")
    plt.show()

    #Prints the number of comparisons for insertion and selections sort
    #This grabs the sorted sets (best case)
    for i in range(100, 10000, 100):
        list = readFile(i, '')
    
        sorted = InsertionSort(list)
    


mode = int(input("Would you like Scatter Plot Mode (1) or User Testing Mode (2)? "))

if(mode == 1):
    scatterplot();
elif(mode == 2):
    userinput();

