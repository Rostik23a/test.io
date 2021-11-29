#Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.




lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))


for num in range(lower,upper + 1):  
   if num > 1:
       for i in range(2,num):  
           if (num % i) == 0:
               s=[num=1]        
               break
       else:
           print(s) 