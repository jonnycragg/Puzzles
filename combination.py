# Rules
# (1) The code consists of 4 digits
# (2) First 3 in descending order
# (3) The sum of the two smallest digits equals 5
# (4) No pair of digits can have a difference of 1
# (5) The product of exactly 1 pair of digits is a prime number
# (6) The code (as a 4 digit number) is divisible by 6
#
# Example
# 4321 - is not the code:
# Passes rules (1) its 4 digits long; (2) first 3 in descending order; (5) only 3*1 is a prime
# Fails rules (3) 2+1=3; (4) 4-3=1 and so does 3-2 and 2-1; (6) its not divisible by 6


# (1) The code consists of 4 digits
import re

def main():
    print("This is the 4 digit combination you are looking for (if 0 non found): " + str(find_combination()))


# Find the 4 digit code
def find_combination():
    ops = 0
    for combination in range(0, 9999, 6):
        ops += 1
        if the_code_is_4_digits_long(str(combination)):
            if first_three_digits_in_descending_order(str(combination)):
                if the_sum_of_the_two_smallest_digits_equals_5(str(combination)):
                    if no_pair_of_digits_can_have_a_difference_of_1(str(combination)):
                        if the_product_of_exactly_1_pair_is_a_prime_number(str(combination)):
                            if the_code_is_divisible_by_6(str(combination)):
                                print("Operations = " + str(ops))
                                return combination
    print("Operations = " + str(ops))
    return 0000

# (1) The code consists of 4 digits
def the_code_is_4_digits_long(code):
    if len(code) == 4:
        return True
    return False


# (2) First 3 in descending order
def first_three_digits_in_descending_order(code):
    if int(code[0]) > int(code[1]) > int(code[2]):
        return True
    return False


# (3) The sum of the two smallest digits equals 5
def the_sum_of_the_two_smallest_digits_equals_5(code):
    sortedCode = ''.join(sorted(code))
    if (int(sortedCode[0]) + int(sortedCode[1])) == 5:
        return True
    return False


# (4) No pair of digits can have a difference of 1
# 4,3,2,1 = 4-3; 4-2, 4-1; 3-2;3-1; 2-1
def no_pair_of_digits_can_have_a_difference_of_1(code):
    index = 1
    for number in code:
        for nextNumber in code[index : len(code) : 1]:
            if int(number)-int(nextNumber) == 1:
                return False
        index += 1
    return True


# (5) The product of exactly 1 pair of digits is a prime number
# 4,3,2,1 = 4-3; 4-2, 4-1; 3-2;3-1; 2-1
def the_product_of_exactly_1_pair_is_a_prime_number(code):
    count = 0
    index = 1
    for number in code:
        for nextNumber in code[index : len(code) : 1]:
            if is_a_prime(int(number)*int(nextNumber)):
                count += 1
        index += 1
    if count == 1:
        return True
    return False

# (6) The code (as a 4 digit number) is divisible by 6
def the_code_is_divisible_by_6(code):
    if int(code) % 6 == 0:
        return True
    return False

# Is this number a prime number
def is_a_prime(n):
    return not re.match(r'^1?$|^(11+?)\1+$', n * '1')

if __name__ == "__main__":
    main()
