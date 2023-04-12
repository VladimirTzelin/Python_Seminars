# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не # является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

EnterNumber = int(input("Введите натуральное число: "))
# Первые элементы ряда Фиб
fib1 = 0
fib2 = 1
fib_n = 0
count = 2
while fib_n < EnterNumber:
    fib_n = fib1 + fib2
    fib1, fib2 = fib2, fib_n
    count += 1
if EnterNumber == fib_n:
    print(f"Число {EnterNumber} является {count} элементом ряда Фибоначчи")
else:
    print(f"Число {EnterNumber} не является элементом ряда Фибоначчи")

# Вариант 2
# a= int(input("Введите число: "))
# if a == 0:
#     print(f"Это {1} элемент ряда Фибоначчи")
# else:
#     fib_prev, fib_next = 0, 1
#     n = 1
#     while fib_next <= a:
#         if fib_next == a:
#             print(f"Это {n} элемент ряда Фибоначчи")
#             break
#         fib_prev, fib_next = fib_next, fib_prev + fib_next
#         n += 1
#     else:
#         print(f"Значения {a} в ряду Фибоначчи нет!")
