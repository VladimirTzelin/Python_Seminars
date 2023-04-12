# Задача №15.
# Иван Васильевич пришел на рынок и решил # купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз # потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

N = int(input("Введите количество арбузов: "))
max = 0
min = 30000
for i in range(N):
    m = int(input("Введите массу арбуза: "))
    if m > max:
        max = m
    if m < min:
        min = m
print(f"Для тёщи надо купить арбуз весом {min} кг, для себя - {max} кг")

# Вариант 2
# mellons = int(input("Введите количество арбузов "))
# i = 0
# min_w = 30000
# max_w = 0
# while i < mellons:
#     mellon_weight = int(input(f"Введите вес арбуза {i+1}: "))
#     if mellon_weight > max_w:
#         max_w = mellon_weight
#     if mellon_weight < min_w:
#         min_w = mellon_weight
#     i += 1
# print(f"Теще арбуз весом {min_w} кг, себе - весом {max_w}, кг")

# Вариант 3
# Arbuz = int(input("Enter arbuz: "))
# VesMin =VesMax= int(input("Ves Arbuz: "))
# for i in range (1, Arbuz):
#     temp = int(input("Ves Arbuz: "))
#     if temp > VesMax:
#         VesMax=temp
#     elif temp < VesMin:
#         VesMin=temp
# print(f"Для тещи {VesMin}, Для себя {VesMax}")

