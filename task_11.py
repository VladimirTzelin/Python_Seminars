# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не # является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

EnterNum = int(input("Введите натуральное число: "))
# Первые элементы ряда Фибоначчи
fib1 = 0
fib2 = 1

fib = 0
count = 2
while fib < EnterNum:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    count += 1
if EnterNum == fib:
    print(f"Число {EnterNum} является {count} элементом ряда Фиббначчи")
else:
    print(f"Число {EnterNum} не является элементом ряда Фиббначчи")