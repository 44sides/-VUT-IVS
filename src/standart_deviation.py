## @file standart_deviation.py
# @brief Calculation of Standart deviation
# @see math_library.Math_library
# @pre The data file consists of a number on each line and it is readable
# @post Printing of standart deviation

from math_library import Math_library as math
import fileinput

N = 0
sum_sqrt_nums = 0
sum_nums = 0

for num in fileinput.input():
    num = float(num)

    N = math.add(N, 1)
    sum_nums = math.add(sum_nums, num)
    sum_sqrt_nums = math.add(sum_sqrt_nums, math.pow(num, 2))

mean = math.div(sum_nums, N)

result = math.n_root(math.div(math.sub(sum_sqrt_nums, math.mul(N, math.pow(mean, 2))), math.sub(N, 1)), 2)

print(result)
