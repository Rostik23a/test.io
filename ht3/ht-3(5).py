 Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z





def balansXY(x,y):
    if x > y:
        print(f'{x} more than {y} on {x-y}')
    elif x < y:
        print(f'{y} more than {x} on {y-x}')
    else:
        print(f'{x} equals {y}')

var_in_X = int(input(' select X ')) 
var_in_Y = int(input(' select Y '))
balansXY(var_in_X, var_in_Y)
