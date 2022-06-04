# frome birthday

from datetime import date
def calculator(birthday):
    today = date.today()
    age = today.year - birthday.year - ((today.month,today.day)< (birthday.month,birthday.day))
    return age

print('your age is : ',calculator(date(2001,4,15)))
#chenges things for new branch
print('you are welcome')