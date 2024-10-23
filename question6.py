# Write a Python function find_greater_than(lst, n) that accepts a list of
# numbers and a number n. The function should return a new list containing only the
# numbers greater than n.

def find_greater_than(list, n):
    return [x for x in list if x > n]

result = find_greater_than([1, 5, 10, 20, 25], 10)
print(result)