"""
def factorial(n:int):
    fact_n = 1
    for i in range (1,n+1):
        fact_n *= i
    return fact_n
"""
array = [10, 20, 30, 40, 50]

for i in range(1, len(array), 2):
    print(array[i])

print("\n")

for i in range(len(array)-1, -1, -1):
    print(array[i])
