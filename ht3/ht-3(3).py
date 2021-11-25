Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)




def season (a):
        if a==12 or a==1 or a==2:
                return "Це зима"
        elif a==3 or a==4 or a== 5:
                return "Це весна"   
        elif a==6 or a==7 or a==8:
                return "Це літо" 
        elif a==9 or a==10 or a==11:
                return "Це осінь"
        elif a==0 or  a > 12:
                return "Такого місяця не має"        
result = season (int(input("Ведіть місяць : ")))
print  (result)       