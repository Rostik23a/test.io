Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.









def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(['Hi', 'world', 22, 11, 2021]))