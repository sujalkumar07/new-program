# Create a function count_vowels(s) that takes a string s as input and returns the number of vowels in the string.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

result = count_vowels("Hello World!")
print(result)