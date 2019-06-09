"""numbers"""
MY_INCOME = 100
TAX_RATE = 0.1
MY_TAXES = MY_INCOME * TAX_RATE
print(MY_TAXES)

# STRINGS Print Formatting
X = "Item One: {x}, Item Two: {y}".format(x="dog", y="cat")
print(X)

# Lists
MATRIX = [
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]
]
# LIST COMPREHENSION
FIRST_COL = [row[0] for row in MATRIX]
print(FIRST_COL)

# Dictionaries
MY_STUFF = {
    "key1": 123,
    "key2": "value2",
    "key3": {"123": [1, 2, "grabMe"]},
    "lunch": "pizza",
    "bfast": "eggs",
    "dinner": "pasta"
}
print(MY_STUFF)

# Sets
X_SET = set()
X_SET.add(1)
X_SET.add(2)
X_SET.add(4)
X_SET.add(0.1)
print(X_SET)
CONVERTED = {1, 1, 2, 2, 4, 4}
print(CONVERTED)

# Exercise
S = 'django'
S_LIST = [
    S[0], S[5], S[:4],
    S[1:4], S[4:], S[::-1]
]
print(S_LIST)
L = [
    3, 7,
    [1, 4, 'hello']
]
L[2][2] = 'goodbye'
print(L)
D1 = {'simple_key': 'hello'}
D2 = {
    'k1': {'k2': 'hello'}
}
D3 = {
    'k1': [
        {'nest_key': ['this is deep', ['hello']]}
    ]
}
D4 = [
    D1['simple_key'],
    D2['k1']['k2'],
    D3['k1'][0]['nest_key'][1][0]
]
print(D4)
AGE = 4
NAME = "Sammy"
AGE_NAME = "Hello, my dog's name is {b} and he is {a} years old".format(a=AGE, b=NAME)
print(AGE_NAME)
