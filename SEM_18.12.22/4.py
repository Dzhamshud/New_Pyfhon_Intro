# Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть служит
# пустая строка.

data = open('file.txt', 'w')
text = input('Введите текст: ')
while text != '':
    data.write(text + '\n')
    text = input('Введите текст: ')
data.close()

