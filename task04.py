from task04_1 import is_float
from task04_1 import is_str

lt = ([2 ** n for n in range(0, 21)])
print('Список 2 в степени N, где N от 0 до 20', lt)

print('Список остатков от деления на 3 чисел из предыдущего списка', [i % 3 for i in lt])

lt = [1, -1, 0, 1.5, -.5, "abc", (1, 4, "vvv"), ["a", "n/a"], "\n", {1: "a", 2: "b"}]
print("Вывожу только числа из списка", lt, "\n", list(lt[i] for i in range(len(lt)) if is_float(lt[i])))

lt = [1, "2", "a+b-c d\ne", [-54, .7, 'qq'], {'a': 1, 'b': 2, 'c': 3}, ('rrr', 'ttt'), "se4s"]
print("Удаляю все небуквенные символы из списка:", lt, "\n", is_str(lt))

lt = {"name": "Bob", "surname": "Bobskyi", "age": 32,
      "position": "Instructor", "Address": "Kudikina gora, 14", "skills": "Lucky"}

print('Исходный словарь', lt)

lt1 = {i: type(lt.get(i)) for i in lt}
print('Новый словарь с такими же ключами, а в значениях типы значений', lt1)

lt2 = {i: "".join(is_str(lt.get(i).lower())) for i in lt if type(lt.get(i)) == str}
print('''Словарь с только парами ключ-значение, если значение исходного словаря было строкой,
значения нового словаря переведены в нижний регистр и удалены всё небуквенные символы:
''', lt2)
