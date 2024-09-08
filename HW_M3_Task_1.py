#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime

def get_days_from_today(date):
    try:
        #Просимо користувача ввести дату
        user_date = input('Введіть дату в форматі РРРР-ММ-ДД: ')
        #Отриману строку конвертуємо в об'єкт datetime
        converted_date = datetime.strptime(user_date, '%Y-%m-%d').date()         
        #Отримуємо поточну дату   
        today_date = datetime.today().date()        
        #Розраховуємо різницю у днях 
        delta_days = today_date - converted_date
        print(f'Кількість днів між заданою датою і поточною датою = {delta_days.days}')  
    except ValueError:
        print('Невірно вказана дата. Для розрахунку запустіть програму та введіть дату в наступному форматі "РРРР-ММ-ДД"')   

get_days_from_today(date='YYYY.MM.DD')
