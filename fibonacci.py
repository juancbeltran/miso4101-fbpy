# encoding: utf-8
# module fibonacci

def fibonacci(x):
    if x == 1:
        return [1, "1"]
    if x == 2:
        return [2, "1, 2"]
    else:
        left = fibonacci(x - 2)
        right = fibonacci(x - 1)
        fibonacciresult = left[0] + right[0]

        return [fibonacciresult, left[1] + ", " + str(right[0]) + ", " + str(fibonacciresult)]


iteraciones = int(input("Iteraciones : "))
result = fibonacci(iteraciones)
print(result[1])
