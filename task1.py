# Вычислить число пи c заданной точностью d

import math

pi = math.pi
d = 0.00001
print(d)
count = 0
while d < 1:
    count += 1
    d = d*10
print(round(pi, count))