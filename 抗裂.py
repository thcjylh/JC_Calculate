import math
import random
import four_homes_and_six_entries as f
from decimal import Decimal

c = random.randint(80, 270)
n = random.randint(3, 7)
b = f.xy(n / 0.48, 0.1)
a = f.xy(c / b, 1)
c = f.xy(a * b, 1)

sum_a = 0
while sum_a != a:
    test = []
    test_w = []
    test_l = []
    for i in range(n):
        temp_w = random.randint(5, 35) / 100
        temp_l = random.randint(100, 580)
        test_w.append(temp_w)
        test_l.append(temp_l)
        test.append(temp_w * temp_l)
    sum_a = f.xy(sum(test) / 2 / n, 1)

print(test_w, sum_a)
print(test_l)
print(a, b, c, n)
