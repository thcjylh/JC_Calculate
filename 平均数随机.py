import random
import four_homes_and_six_entries as f

x_d = 9.6 # 目标平均值
n = 6  # 样本数
test_x = []
aver = 0
while aver != x_d:
    test_x = []
    for i in range(n):
        temp = f.xy(x_d + random.randint(-70, 70)/100, 0.1)
        test_x.append(temp)
    aver = f.xy(sum(test_x) / len(test_x), 0.1)
print(test_x)
