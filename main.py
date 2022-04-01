# task_1
print('task_1')
p = 7
x = 7
while x < 46:
    x += 3
    p += x
print(f'p = {p}')

# task_2
print('\ntask_2')
k = -4
P = 1
while k < 6:
    k += 1
    P *= abs(k-7) / 5
print(f'P = {P}')

# task_3
print('\ntask_3')
n = 0
sum_ = 0
q = 0
while n < 11:
    n +=1
    a = float(input('Введіть число: '))
    if a > 5:
        sum_ += a
        q += 1
print(f'Сума чисел білших за 5 = {sum_}')
print(f'Кількість чисел білших за 5 = {q}')