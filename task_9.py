# Задача №9.
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

nFact = int(input("Введите число для вычисления N! > "))
if (nFact < 0):
    print("Введите целое не отрицательное число")
else:
    fact = 1
    i = 1
    while i <= nFact:
        fact = fact * i
        i += 1
    print(f"Факториал {nFact} равен {fact}")

# # Вариант 2
# number = tempNumber = int(input("Введите n : "))
# # Проверка ввода значения 0
# if number == 0:
#     print(f"факториал {number} = 1")
# else:
#     factorialNumber = 1

#     while (tempNumber != 1):
#         factorialNumber *= tempNumber
#         tempNumber -= 1

#     print(f"факториал {number} = {factorialNumber}")

# Вариант 3
# n = int(input("Введите n: "))
# i = 1
# num = 1
# while i < n:
#     i += 1
#     num = num * i
# print(num)
