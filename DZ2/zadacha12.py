# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает 
# два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет
# сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2   5 6 -> 2 3

total = int(input('Введите сумму задуманных чисел '))
product = int(input('Введите произведение задуманных чисел '))
flag = False
for i in range(1, 1001):
    for j in range(1, 1001):
        if i + j == total and i * j == product:
            flag = True
            x = i
            y = j
        j += 1
    i += 1
if flag:
    print('Петя задумал числа {} и {}.'.format(x, y))
else:
    print('К сожалению, Петя не смог подобрать целые числа.')