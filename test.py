import math
from decimal import Decimal
import random
import openpyxl
import time
import four_homes_and_six_entries as f
import numpy

s=[0]
for i in range(10,500):
    a=f.xy(Decimal(i)/Decimal(100)*Decimal(3.545)*Decimal(0.01),0.001)
    if a!=s[len(s)-1]:
        s.append(a)
print(s)

