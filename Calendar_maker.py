import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')


def main():
    year = int(input("Enter the year you want to create the calendar for:\n>   "))
    month = int(input("Enter the month you want to create the calendar for (1-12):\n>   "))
    currentDate = datetime.date(year, month, 1)
    
    while currentDate.weekday() != 0:
        currentDate -= datetime.timedelta(days=1)
    print_calendar(currentDate)


def print_calendar(beginningCal: datetime.date) -> None:
    calText = ''
    calText += ' '*34 + f'{MONTHS[beginningCal.month]}' + f' {beginningCal.year}\n'
    calText += '...Monday....Tuesday...Wednesday...Thursday....Friday....Saturday.....Sunday..\n'
    
    weekSeparator = ('+----------'*7) + '+\n'
    calRow = ('|          '*7) + '|\n'
    
    calText += weekSeparator
    for weeks in range(6):
        for days in range(7):
            calText += (f'|{beginningCal.day}' + ' '*9) if beginningCal.day//10 < 1 else (f'|{beginningCal.day}' + ' '*8)
            beginningCal += datetime.timedelta(days=1)
        calText += '|\n'
        calText += calRow*3
        calText += weekSeparator
    print(calText)


if __name__ == '__main__':
    main()