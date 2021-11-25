print("Нуль як знак операці"
      "\n завершить роботу програми")
while True:
    s = input("Знак < , >, = : ")
    if s == '0':
        break
    if s in ('<','>''='):
        x = float(input("x"))
        y = float(input("y"))
        if s == '<':
            print("%.2f" % (x<y))
        elif s == '>':
            print("%.2f" % (x>y))
        elif s == '=':
            print("%.2f" % (x=y))
