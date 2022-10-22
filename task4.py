# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

koefs = []
k = int(input("Степень многочлена: "))
koefs = [randint(0, 100) for _ in range(k+1)]
print(koefs)

res = ''
for i, koef in enumerate(koefs):
    if len(res) > 0 and koef > 0:
        res = res + '+'
    if koef == 0:
        continue
    if k - i != 1:
        res = res + str(koef) + 'x^' + str(k-i)
    else:
        res = res + str(koef) + 'x'

if koefs[-1] != 0:
    res = res[:len(res) - 3]

res = res + ' = 0'
print(res)

with open('file.txt', 'w') as f:
    f.write(res)