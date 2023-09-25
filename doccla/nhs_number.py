import random
import sys


def check_sum(str_num: str):
    multiplier = 10
    i = 0
    res = 0
    while i < 9:
        res += (int(str_num[i]) * multiplier)
        i += 1
        multiplier -= 1
    return res % 11


def handle_validate(str_num):
    mod_11 = check_sum(str_num)
    is_valid = str(mod_11) == str_num[9]
    if not is_valid:
        return f"Not a valid NHS number: {str_num}"
    return f"Valid NHS number: {str_num}"


def generate_valid_number():
    rand_number = ""
    for _ in range(9):
        rand_number += str(random.randint(0, 9))
    return rand_number + str(check_sum(rand_number))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"New Valid Number: {generate_valid_number()}")
        exit(0)
    if len(sys.argv) > 2:
        print("You may only provide one argument - a 10 digit number")
        exit(2)
    num = str(sys.argv[1])
    if not num.isnumeric() or len(num) != 10:
        print("Argument must be a 10 digit number")
        exit(2)
    print(handle_validate((num)))
