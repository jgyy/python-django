"""Function Exercises"""


def array_check(nums):
    """
    :param nums: numbers
    """
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[1 + 2] == 3:
            return True
    return False


def string_bits(my_string):
    """
    :param my_string: strings
    """
    result = ""
    for (i, char) in enumerate(my_string):
        if i % 2 == 0:
            result += char
    return result


def end_other(str_a, str_b):
    """
    :param str_a: string 1
    :param str_b: string 2
    """
    str_a = str_a.lower()
    str_b = str_b.lower()
    return str_b.endswith(str_a) or str_a.endswith(str_b) or \
        str_a[-(len(str_b)):] == str_b or str_a == str_b[-len(str_a):]


def double_char(my_string):
    """
    :param my_string: strings
    """
    result = ''
    for char in my_string:
        result += char*2
    return result


def no_teen_sum(num_a, num_b, num_c):
    """
    :param num_a: number 1
    :param num_b: number 2
    :param num_c: number 3
    """
    return fix_teen(num_a) + fix_teen(num_b) + fix_teen(num_c)


def fix_teen(num):
    """
    :param num: number
    """
    if num in [13, 14, 17, 18, 19]:
        return 0
    return num


def count_evens(nums):
    """
    :param nums: array of numbers
    """
    count = 0
    for element in nums:
        if element % 2 == 0:
            count += 1
    return count


print(
    array_check([1, 1, 2, 3, 1]),
    array_check([1, 1, 2, 4, 1]),
    array_check([1, 1, 2, 1, 2, 3])
)
print(
    string_bits('Hello'),
    string_bits('Hi'),
    string_bits('Heeololeo')
)
print(
    end_other('Hiabc', 'abc'),
    end_other('AbC', 'HiaBc'),
    end_other('abc', 'abXabc')
)
print(
    double_char('The'),
    double_char('AAbb'),
    double_char('Hi-There')
)
print(
    no_teen_sum(1, 2, 3),
    no_teen_sum(2, 13, 1),
    no_teen_sum(2, 1, 14)
)
print(
    count_evens([2, 1, 2, 3, 4]),
    count_evens([2, 2, 0]),
    count_evens([1, 3, 5])
)
