#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime

def get_days_from_today(date):
    try:        
        #Отриману строку конвертуємо в об'єкт datetime
        converted_date = datetime.strptime(date, '%Y-%m-%d').date()         
        #Отримуємо поточну дату   
        today_date = datetime.today().date()        
        #Розраховуємо різницю у днях 
        delta_days = today_date - converted_date        
    except ValueError:
        return 'Error! String not format YYYY.MM.DD!'      
    except UnboundLocalError:
        return 'Error! String not format YYYY.MM.DD!'  

    return delta_days
