#Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.




def is_prime(n):
    if n < 2:
        return False
    elif n==2:
        return True
    limit = n**(1/2)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True
print(is_prime(int(input("numeric : "))))