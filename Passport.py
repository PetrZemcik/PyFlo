import time
current_year = int(time.strftime('%Y'))
print('The current year is', current_year)
received_year = int(input('What year did you get your passport? '))
print('You received your passport in', received_year)
if received_year + 10 < current_year:
    print('You should go get a new passport')
else:
    print('You may use your current passport')