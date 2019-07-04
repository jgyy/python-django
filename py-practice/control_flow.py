"""Comparison Operators"""
COMPARE = [
    1 > 2,
    1 < 2,
    1 <= 4,
    1 == "1",
    "h1" == "bye",
    1 != 2
]
print(COMPARE)

# Logical Operators
LOGICAL = [
    (1 > 2) and (2 < 3),
    (1 > 2) or (2 < 3),
    (1 == 2) or (2 == 3)
]
print(LOGICAL)
if 1 < 2:
    print('First Block')
    if 2 < 3:
        print('Second Block')

# For Loops
SEQ = [1, 2]
D = {"Sam": 1, "Frank": 2, "Dan": 3}
for item in SEQ:
    print(item)
for item in D:
    print(item, D[item])
MY_PAIRS = [(1, 2), (3, 4), (5, 6)]
for (tup1, tup2) in MY_PAIRS:
    print(tup2, tup1)
WHILE_I = 1
while WHILE_I < 4:
    print("'I' is: {}".format(WHILE_I))
    WHILE_I += 1
for item in range(0, 10, 4):
    print(item)
# List Comprehension
X = [1, 2, 3, 4]
OUT = []
for num in X:
    OUT.append(num**2)
print(OUT)


def my_func(param1, num1, num2):
    """This is the docstring"""
    if isinstance(num1, int) == isinstance(num2, int):
        num3 = num1 + num2
    else:
        num3 = "Sorry, I need integers!"
    return (
        "my first python function! {}".format(param1),
        num3
    )


RESULT_STRING, RESULT_NUMBER = my_func("a", "b", 33)
print(RESULT_STRING, RESULT_NUMBER)
# Lambda Expression
# Filter
MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8]
EVENS = filter(lambda x: x % 2 == 0, MY_LIST)
print(list(EVENS))
TWEET = "Go Sports! #Sports"
RESULT = TWEET.split('#')
print(RESULT, 'x' in [1, 2, 3, 'x'])
