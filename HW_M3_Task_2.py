#2. Необхідно написати функцію get_numbers_ticket(min, max, quantity), \
# яка генерує набір унікальних випадкових чисел у межах заданих параметрів

from random import randint

#Створюємо функцію для генерації унікальних випадкових чисел
def get_numbers_ticket(min, max, quantity):

    #Створюємо пусту множину
    result = set()

    if min < 1 and max > 1000 and quantity >= (max-min): 
        return 'Значення min повинно бути не менше за 1, max - не більше за 1000, quantity - не більше за різницю між max та min!'
    elif min < 1 and max > 1000:
        return 'Значення min повинно бути не менше за 1, а max - не більше за 1000!'  
    elif min < 1 and quantity >= (max-min):  
        return 'Значення min повинно бути не менше за 1, а quantity - не більше за різницю між max та min!'   
    elif max > 1000 and quantity >= (max-min):  
        return 'Значення max повинно бути не більше за 1000, а quantity - не більше за різницю між max та min!'
    elif max > 1000:
        return 'Значення max повинно бути не більше за 1000!'
    elif min < 1:
        return 'Значення min повинно бути не менше за 1!'
    elif max < min:
        return 'Значення max повинно бути більше за min!'        
    elif quantity >= (max-min):
        return 'Значення quantity повинно бути не більше за різницю між max та min!'             
    else:
        while len(result) != quantity:            
            result.add(randint(min, max))

    return sorted(result)
