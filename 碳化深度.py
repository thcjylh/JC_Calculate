import random
import four_homes_and_six_entries as f


x_d = 3.0
test_x = []
aver = 0
while aver != x_d:
    test_x = []
    for i in range(9):
        temp = f.xy(x_d + 0.5 * random.randint(-1, 1), 0.5)
        test_x.append(temp)
    aver = f.xy(sum(test_x) / len(test_x), 0.1)
print(test_x,x_d)
