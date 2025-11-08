# 1 -  misol
strings = ["salom", "dunyo", "python", "AI"]
lengths = list(map(lambda s: len(s), strings))
print(lengths)


# 2 - misol
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print(odd_squares)


#3 - misol
numbers = [2, 4, 6, 8]
indexed = list(map(lambda x: x[0] * x[1], enumerate(numbers)))
print(indexed)


# 4 - misol
palindrome = lambda s: s == s[::-1]
words = ["level", "python", "anna", "chatgpt"]
results = list(map(lambda w: (w, palindrome(w)), words))
print(results)

# 5 - misol
numbers = [1, 3, 5, 6, 8, 10, 12]
filtered = list(filter(lambda x: 5 < x < 10, numbers))
multiplied = list(map(lambda x: x * 3, filtered))
print(multiplied)
