# Define a function find_maximum(a, b) that accepts two numbers and returns the larger number.

def find_maximum(a, b):
    return a if a>b else b
max_value = find_maximum(10, 5)
print(max_value)