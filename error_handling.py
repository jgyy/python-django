"""Error Handling"""
import re
from mymodule import func_in_module

try:
    F = open('simple.txt', 'w')
    F.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")

PATTERNS = ['term1', 'term2']
TEXT = 'This is a string with term1, not not the other!'
for pattern in PATTERNS:
    print("I'm searching for: " + pattern)
    match = re.search(pattern, TEXT)
    if match:
        print("MATCH!", match.start())
    else:
        print("NO MATCH!")
SPLIT_TERM = '@'
EMAIL = 'user@gmail.com'
print(re.split(SPLIT_TERM, EMAIL))
print(re.findall('match', 'test phrase match in match middle'))


def multi_re_find(patterns, phrase):
    """
    :param patterns:
    :param phrase:
    """
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")


TEST_PHRASE = "This is a string with numbers 12312 and a symbol #hashtag"
TEST_PATTERNS = [r'\S+']
multi_re_find(TEST_PATTERNS, TEST_PHRASE)
func_in_module()