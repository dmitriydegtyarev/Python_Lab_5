from check_number import check_number

def fibonacci_sequence():

    """
    Перші два елементи списку F0=1, F1=1.
    Послідовність повинна починатися згідно з умовою F0=1, F1=1, F2=1, Fn=Fn-1+Fn-2, n>=2
    """

    fib = [0, 1]
    n = check_number()

    """
    F2 = 1 так як F0 + F1 = 1, F3 = 2 так як F1 + F2 = 2 і т.д.
    """

    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return print("Послідовність Фібоначчі:", fib)

fibonacci_sequence()