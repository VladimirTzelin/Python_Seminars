# Задача №21.
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

dict = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ",
        " V ": " S009 ", " VIII ": " S007 ", "IV": "holla", "1234": "S005"}
values = list(dict.values())
print(values)
unique_values = set(values)
print(unique_values)