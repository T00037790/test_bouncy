# /usr/bin/python3
# --------- BOUNCY NUMBERS -------------------->
import unittest


def increasing(lst, length):
    flag = 0
    for i in range(length - 1):
        if lst[i + 1] >= lst[i]:
            flag = 0
        else:
            flag = 1
            return False
    if flag == 0:
        return True


def decreasing(lst, length):
    flag = 0
    for i in range(length - 1):
        if lst[i + 1] <= lst[i]:
            flag = 0
        else:
            flag = 1
            return False
    if flag == 0:
        return True


def main():
    total = 100
    bouncy = 0
    ratio = 0

    while ratio != 0.99:
        lst = list(str(total))
        if not increasing(lst, len(lst)) and not decreasing(lst, len(lst)):
            bouncy += 1
        ratio = bouncy / total
        total += 1

    total -= 1
    print("number that meets the requirements is ")
    return total


class TestBouncy(unittest.TestCase):

    def test_function_receive_a_list_and_a_int_and_return_boolean(self):
        assert type(increasing([1, 2, 3, 4, 5], 5)) is bool and type(decreasing([5, 4, 3, 2, 1], 5)) is bool

    def test_main_function_return_int(self):
        assert type(main()) is int


if __name__ == '__main__':
    unittest.main()

