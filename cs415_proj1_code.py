
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
        return 1
    
    mult += 1
    curr_val, mult = 
    return a * expo_dec_by_one(a, n-1, mult)

def expo_dec_by_const(a, n, mult):
    if n == 0:
        return 1
    
    elif n % 2 == 0:
        mult += 1
        curr_val, mult = expo_dec_by_const(a, n//2, mult)
        return ( ** 2)
    
    else:
        mult += 1
        curr_val, mult = 
        return (expo_dec_by_const(a, (n-1)//2, mult) ** 2) * a


def expo_div_and_conq(a, n, mult):
    if n == 0:
        return 1
    
    elif n % 2 == 0:
        mult += 1
        curr_val, mult = expo_dec_by_const(a, n//2, mult)
        curr_val, mult = expo_dec_by_const(a, n//2, mult)
        return 
    
    else:
        mult += 1
        curr_val, mult = 
        curr_val, mult = 
        return (expo_dec_by_const(a, n//2), mult ** 2) * a


def userinput():
    i = int(input("What is your kth number you would like to compute "))

    NumAdditions = 0
    numComp = 0

    FibNumber, NumAdditions = fib(i, NumAdditions)

    m, NumAdditions = fib(i + 1, NumAdditions)

    n, NumAdditions = fib(i, NumAdditions)

    modulo_div = euclids(m, n, numComp)


    print("kth fibonacci term is ", FibNumber)
    print("Num additions is ", NumAdditions)
    print("The number of modulo divisions is ", modulo_div)

    print()

    base = int(input("For exponentiation would would you like your base to be? "))

    exponent = int(input("What would you like your exponent to be? "))

    by_one, mult = expo_dec_by_one(base, exponent)
    by_const, mult = expo_dec_by_const(base, exponent)
    div_conq, mult = expo_div_and_conq(base, exponent)



    print("Decrease by one outputs", by_one)

    print("Decrease by a constant outputs", by_const)

    print("Divide and conquire outputs", div_conq)


    

def scatterplot():

    NumAdditions = 0
    numComp = 0

    print("(k, A(k))")

    for i in range (0, 40, 5):
        FibNumber, NumAdditions = fib(i, NumAdditions)
        
        print("(", i, ", ", NumAdditions, ")")

    print()
    print("(n, D(N))")

    for i in range (0, 40, 5):
        m, NumAdditions = fib(i + 1, NumAdditions)
        n, NumAdditions = fib(i, NumAdditions)
        

        modulo_div = euclids(m, n, numComp)

        print("(", n, ", ", modulo_div, ")")

    
    print()
    print("(n, M(n))")
    
    base = 4

    for i in range (0, 40, 5):

        by_one, one_mult = expo_dec_by_one(base, i)
        by_const, cont_mult = expo_dec_by_const(base, i)
        div_conq, conq_mult = expo_div_and_conq(base, i)

        print("(", i, ", ", one_mult, ")")
        print("(", i, ", ", cont_mult, ")")
        print("(", i, ", ", conq_mult, ")")


    


mode = int(input("Would you like Scatter Plot Mode (1) or User Testing Mode (2)?"))

if(mode == 1):
    scatterplot();
elif(mode == 2):
    userinput();

