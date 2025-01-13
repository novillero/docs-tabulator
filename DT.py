file = input('Введите название файла:')
f = open(file, 'r', errors='replace', encoding='utf-8')
lines = f.readlines()
number = input('Введите номера строк (отдельные строки через запятую, диапазоны строк через дефис):')
number = number.split(sep = ',')
stroke = []
for item in number:
    if '-' in item:
        item = item.split(sep = '-')
        item = map(int, item)
        start, end = item
        stroke.extend(range(start, end + 1))
    else:
        item = int(item)
        stroke.append(item) 

ws = int(input('Сколько пробелов добавить? Введите целое число:'))

for i in range(len(lines)):
    if i+1 in stroke:
        lines[i] = ws * ' ' + lines[i]
    else:()

f = open(file, 'w', errors='replace', encoding='utf-8')
f.writelines(lines)

f.close()

print('Файл обновлён.')