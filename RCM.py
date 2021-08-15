import random
from sympy import *
import four_homes_and_six_entries as f
from decimal import Decimal

l = random.randint(485, 515) / 10
d = random.randint(995, 1005) / 10
u = int(input('电压：'))
d_rcm = float(input('测定值：'))
t0 = random.randint(208, 215) / 10
t1 = random.randint(198, 203) / 10
delta_t = f.xy((t1 + t0) / 2, 0.1)
t = 24  # 测试时间24h，根据电压变化
x = Symbol('x')
x_d = solve(
    [(0.0239 * (273 + delta_t) * l) / (u - 2) / t * (x - 0.0238 * ((273 + delta_t) * l * x / (u - 2)) ** 0.5) - d_rcm],
    [x])
x_d = f.xy(x_d[0][0], 0.1)
print(l, d, u, t0, t1, delta_t, t)
test_x = []
aver = 0
while aver != x_d:
    test_x = []
    for i in range(7):
        temp = f.xy(x_d * random.randint(93, 107) / 100, 0.1)
        test_x.append(temp)
    aver = f.xy(sum(test_x) / len(test_x), 0.1)
print(test_x)
print(x_d)
print(d_rcm)
