

def factorials(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


n = int(input('факториалы: '))
print(list(factorials(n)))
