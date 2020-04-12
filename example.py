#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print('work 1')
z = 0
for z in range (0,5):
  z += 1
  print('String', z,"is 0")

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('work 2')

sum = 0
for i in range (10):
    i = int (input('Enter the digits!:'))
    if i == 5:
        sum += 1
print('Number five-', sum)
print('Thanks')
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print('Work 3')
sum = 0
for i in range(1,101):
    sum += i
    print(sum)


'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print('Work 4')
sum = 1
for i in range(1,11):
    sum *= i
    print(sum)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print('Work 5')

integer_number = 2129

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
print('')

'''
Задача 6
Найти сумму цифр числа.
'''
print('Work 6')

integer_number = 21115
sum = 0
while integer_number>0:
   sum += integer_number%10
   integer_number = integer_number // 10
print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
print('Work 7')

integer_number = 11214
sum = 1
while integer_number>0:
   sum *= integer_number%10
   integer_number = integer_number // 10
print(sum)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print('Work 8')

integer_number = 213513
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
print('Work 9')

integer_number = 364395
i = 0
while integer_number > 0:
    if integer_number%10 > i:
        i = integer_number%10
    integer_number = integer_number//10
print(i)

'''
Задача 10
Найти количество цифр 5 в числе
'''

print('Work 10')

integer_number = 355559555
i = 0
while integer_number > 0:
    if integer_number%10 == 5:
       i+= 1
    integer_number = integer_number//10
print(i)

print('THE END')