#2. Необхідно написати функцію get_numbers_ticket(min, max, quantity), \
# яка генерує набір унікальних випадкових чисел у межах заданих параметрів

from random import randint

#Просимо користувача заповнити параметри
min = int(input('Введіть значення min: '))
max = int(input('Введіть значення max: '))
quantity = int(input('Введіть значення quantity: '))

#Створюємо пусти множину
result = set()

#Створюємо функцію для генерації унікальних випадкових чисел
def get_numbers_ticket(min, max, quantity):
    if min < 1 and max > 1000:  
        print('Значення min повинно бути не менше за 1, а max - не більше за 1000!')
    elif max > 1000:
        print('Значення max повинно бути не більше за 1000!')
    elif min < 1:
        print('Значення min повинно бути не менше за 1!')  
    else:
        while len(result) != quantity:            
            result.add(randint(min, max))  
        print(sorted(list(result)))  
  
get_numbers_ticket(min, max, quantity)
