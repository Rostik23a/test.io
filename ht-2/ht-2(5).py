

dict_1 = {1:10, 2:20, 3:30, 4:40, 5:30, 6:60}
temp = []
res = dict()
for key, val in dict_1.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
  
print("Словник після видалення значень : " + str(res)) 