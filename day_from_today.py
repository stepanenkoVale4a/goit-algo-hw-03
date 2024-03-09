from datetime import datetime
date_string = input("Date in format YYYY-MM-DD")

def get_days_from_today(date_string):
    try:
        date_dt = datetime.strptime(date_string, "%Y-%m-%d")
        today_dt = datetime.today()
        result = today_dt - date_dt
        return result.days
    except ValueError:
        print('Incomming date format was incorrect')
        
print(get_days_from_today(date_string))