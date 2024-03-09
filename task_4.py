from datetime import datetime, timedelta
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Black", "birthday": "1986.04.13"},
    {"name": "Joahne White", "birthday": "1998.03.07"}
]

def find_next_weekday(d, weekday : int):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead +=7
    return d + timedelta(days=days_ahead)


def get_upcoming_birthdays(users):
    prepared_users = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            prepared_users.append({"name":user['name'], 'birthday':birthday})
        except ValueError:
            print(f'Format not correct for user {user["name"]}')
        

    days = 7
    today = datetime.today().date()
    upcomming_birthdays = []
    for user in prepared_users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year +1)
        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday >=5: #вихідні дні
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcomming_birthdays.append({
                "name":user["name"],
                "congratulation_date": congratulation_date_str
            })
    print(upcomming_birthdays)
    
get_upcoming_birthdays(users)

