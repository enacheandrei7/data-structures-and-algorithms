"""
Fibonacci sequence using a simple explanatory method and a recursion method
"""

# Slower method, with no recursion
def fibonacci(num):
    """
    Fibonacci sequence implementation in a simple, explanatory way
    """
    if num < 2:
        return num
    first_el = 0
    second_el = 1
    total = 0
    for _ in range(num-1):
        total = first_el+second_el
        first_el = second_el
        second_el = total
    return total


# Recursive method
def fibonacci_recur(num):
    """
    Fibonacci sequence algorithm using recursivity
    """
    if num < 2:
        return num
    else:
        return fibonacci_recur(num-1) + fibonacci_recur(num-2)


# Recursive method cached
CALCULATIONS = 0
CACHE = {}
def fibonacci_recur_cached(num):
    """
    Fibonacci sequence algorithm using recursivity and cached value
    for less time complexity (faster execution)
    """
    global CALCULATIONS
    if num in CACHE:
        CALCULATIONS+=1
        # print(CALCULATIONS)
        # print(CACHE)
        return CACHE[num]
    else:
        if num < 2:
            return num
        else:
            CACHE[num] = fibonacci_recur_cached(num-1) + fibonacci_recur_cached(num-2)
            return CACHE[num]


print("Explanatory method: ", [fibonacci(i) for i in range(11)])
print("Recursive method: ", [fibonacci_recur(i) for i in range(11)])
print("Recursive method cached first time: ")
print([fibonacci_recur_cached(i) for i in range(11)])
print("Recursive method cached second time: ")
CALCULATIONS = 0
print([fibonacci_recur_cached(i) for i in range(11)])
print("Fibonacci numbers: ", [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
