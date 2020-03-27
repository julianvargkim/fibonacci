# This assumes that for [1,1,2,3,5,8], n-value would be [1,2,3,4,5,6]
# For example, fibonacci(3) should return 2.
import datetime


def fibonacci(n: int):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


cache = {}


def mem_fibonacci(n: int):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    value = mem_fibonacci(n-1) + mem_fibonacci(n-2)
    cache[n] = value
    return value


def fibonacci_example(n: int):
    if type(n) != int:
        raise TypeError("fibonacci_example: only positive integer allowed.")
    if n < 1:
        raise ValueError("fibonacci_example: only positive integer allowed.")

    # Optimized fibonacci
    print("Fibonacci optimized (caching) starting...")
    start = datetime.datetime.now()
    result = mem_fibonacci(n)
    print("Result: " + str(result))
    print("Time: " + str((datetime.datetime.now() - start)))

    # Not optimized fibonacci
    print("Fibonacci not optimized (no caching) starting...")
    start = datetime.datetime.now()
    result = fibonacci(n)
    print("Result: " + str(result))
    print("Time: " + str((datetime.datetime.now() - start)))


fibonacci_example(30)
