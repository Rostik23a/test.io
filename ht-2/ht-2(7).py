Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
                Приклад словника (можете використовувати свій):
                dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}





dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key_min = min(dict_1.keys(), key=(lambda k: dict_1[k]))
key_max = max(dict_1.keys(), key=(lambda k: dict_1[k]))

print('Max: ',dict_1[key_max])
print('Min: ',dict_1[key_min])