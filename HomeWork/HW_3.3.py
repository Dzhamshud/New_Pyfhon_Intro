# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = [1.1, 1.2, 3.1, 5, 10.01]
max_drob = a[0]%1
min_drob = a[0]%1
for i in range(1, len(a)):
    if a[i]%1>max_drob:
        max_drob=a[i]%1
    elif a[i]%1<min_drob:
        min_drob=a[i]%1
print(max_drob-min_drob)
