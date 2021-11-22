def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(['Hi', 'world', 22, 11, 2021]))