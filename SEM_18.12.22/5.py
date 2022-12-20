# Напишите программу, которая определит позицию второго вхождения строки
# в списке либо сообщит, что её нет.

lst = ['abc', '123', 'sldk', 'abc', 'dsfj', '123', '654', 'abc']
count = 0
i = 0
index = 0
st = '111'
for elem in lst:
    i +=1
    if st == elem:
        count +=1
        if count == 2:
            index = i
            break
        elif count < 2:
            continue            
if index<2:
    print(f'Второго вхождения строки {st} нет')
else:
    print(index)