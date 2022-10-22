# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = 756
lst = []
div = 2
while n > 1:
    if n % div == 0:
        lst.append(div)
        n = n / div
        div = 2
    else:
        div += 1
print(lst)