import math
from decimal import Decimal
import random
import openpyxl
import time
import four_homes_and_six_entries as f
import numpy


# 引用的函数
def ascii_str(asc):  # ASCII码循环
    if asc <= 90:
        return chr(asc)
    else:
        return chr(((asc - 64) // 26) * 1 + 64) + chr((asc - 65) % 26 + 65)


def cracking(grade):
    temp_w = []  # 记录裂缝宽度
    temp_l = []  # 记录裂缝长度
    c = random.randint(round(grade * 0.8), round(grade * 1.2))  # 随机化抗裂等级
    n = random.randint(3, 7)  # 裂纹条数
    b = float(f.xy(Decimal(n) / Decimal('0.48'), 0.1))  # b:单位面积的裂纹数目，0.48为平板面积
    a = int(f.xy(Decimal(c) / Decimal(b), 1))  # a:每条裂纹的平均开裂面积
    sum_a = 0  # 计算随机生成数据的a（每条裂纹的平均开裂面积）
    while sum_a != a:  # 当随机生成数据的a与设定值不符时运行以下：
        temp_sum = []  # 记录Σ（w*i)
        temp_w = []  # 记录裂缝宽度
        temp_l = []  # 记录裂缝长度
        for i in range(n):
            crack_w = random.randint(round(c/100), round(c/10)) / 100  # 随机生成裂缝宽度（0.03mm~0.35mm）
            crack_l = random.randint(100, 580)  # 随机生成裂缝长度（100mm~500mm）
            temp_w.append(crack_w)
            temp_l.append(crack_l)
            temp_sum.append(crack_w * crack_l)
        sum_a = f.xy(sum(temp_sum) / 2 / n, 1)
    a = sum_a
    c = int(f.xy(Decimal(a) * Decimal(b), 1))  # c:单位面积上的总开裂面积
    if c < 100:
        c_grade = 'L-Ⅴ'
    elif 100 <= c < 400:
        c_grade = 'L-Ⅳ'
    elif 400 <= c < 700:
        c_grade = 'L-Ⅲ'
    elif 700 <= c < 1000:
        c_grade = 'L-Ⅱ'
    elif c >= 1000:
        c_grade = 'L-Ⅰ'
    else:
        c_grade = 'Error'
    return a, b, c, n, c_grade, temp_w, temp_l


crack_grade = 256
template_dir = 'E:/文档/10.数据计算/混凝土耐久性/耐久性.xlsx'  # 表格模板路径地址

wb = openpyxl.load_workbook(template_dir)  # 打开文档
my_sheet = wb.get_sheet_by_name('抗裂')
for i in range(2):
    item = cracking(crack_grade)
    for j in range(3):
        my_sheet[ascii_str(87 + 2 * i) + str(24 + j)] = item[j]
    my_sheet['T' + str(4 + 9 * i)] = item[3]
    for j in range(item[3]):
        my_sheet['D' + str(4 + i * 9 + j)] = str(j + 1)
        my_sheet['L' + str(4 + i * 9 + j)] = str(j + 1)
    for j in range(item[3]):
        my_sheet['F' + str(4 + i * 9 + j)] = item[5][j]
        my_sheet['N' + str(4 + i * 9 + j)] = item[6][j]
my_sheet['AA26'] = f.xy((my_sheet['W26'].value + my_sheet['Y26'].value) / 2, 1)  # 抗裂等级代表值
if int(my_sheet['AA26'].value) < 100:  # 判断抗裂等级，抗裂等级L-Ⅴ
    my_sheet['AD24'].value = 'L-Ⅴ'
elif 100 <= int(my_sheet['AA26'].value) < 400:  # 抗裂等级L-Ⅳ
    my_sheet['AD24'].value = 'L-Ⅳ'
elif 400 <= int(my_sheet['AA26'].value) < 700:  # 抗裂等级L-Ⅲ
    my_sheet['AD24'].value = 'L-Ⅲ'
elif 700 <= int(my_sheet['AA26'].value) < 1000:  # 抗裂等级L-Ⅱ
    my_sheet['AD24'].value = 'L-Ⅱ'
elif int(my_sheet['AA26'].value) >= 1000:  # 抗裂等级L-Ⅰ
    my_sheet['AD24'].value = 'L-Ⅰ'
else:  # 抗裂等级错误
    my_sheet['AD24'] = my_sheet['AA26'].value

wb.save(template_dir[0:-5] + time.strftime('%Y-%m-%d %H%M%S', time.localtime()) + '.xlsx')  # 保存文档
