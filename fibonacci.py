def fibonacci_recursive(n):
    # Base cases: 0th is 0, 1st is 1
    if n <= 1:
        return n
    # Recursive step: call itself for the previous two numbers
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Print the first 10 numbers using a list comprehension
print([fibonacci_recursive(i) for i in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
