class Date:
    name_months = ['янв', 'фев', 'мар', 'апр',
                        'май', 'июн', 'июл', 'авг',
                        'сен', 'окт', 'ноя', 'дек']
    
    def __init__(self, date):
        try:
            day, month, year = map(str, date.split('.'))
            if len(str(day)) != 2 or len(str(month)) != 2 or not (1 <= int(month) <= 12 and 1970 <= int(year) <= 2024):
                raise ValueError
            
            day, month, year = int(day), int(month), int(year)
            if ((month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= day <= 31)) or
                (month in [4, 6, 9, 11] and not (1 <= day <= 30)) or
                (month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and not (1 <= day <= 29)) or
                (month == 2 and not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and not (1 <= day <= 28))):
                raise ValueError
            self.__date = date

        except (ValueError, AttributeError):
            self.__date = None
            print('ошибка')


    @property
    def date(self):
        if self.__date:
            day, month, year = map(int, self.__date.split('.'))
            return f'{day} {Date.name_months[month - 1]} {year} г.'
        else:
            return None

    @date.setter
    def date(self, date):
        try:
            day, month, year = map(str, date.split('.'))
            if len(str(day)) != 2 or len(str(month)) != 2 or not (1 <= int(month) <= 12 and 1970 <= int(year) <= 2024):
                raise ValueError
            
            day, month, year = int(day), int(month), int(year)
            if ((month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= day <= 31)) or
                (month in [4, 6, 9, 11] and not (1 <= day <= 30)) or
                (month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and not (1 <= day <= 29)) or
                (month == 2 and not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and not (1 <= day <= 28))):
                raise ValueError
            self.__date = date

        except (ValueError, AttributeError):
            self.__date = None
            print('ошибка')

    def to_timestamp(self):
        day_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.__date:
            day, month, year = map(int, self.__date.split('.'))
            years = year - 1970
            months = sum(day_months[:month - 1])
            leap_year = years // 4 - years // 100 + years // 400
            days = (day - 1) + leap_year
            if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                days += 1
            seconds = (years * 365 + months + days) * 24 * 60 * 60
            return seconds
        else:
            return None

    def __lt__(self, other):
        return self.to_timestamp() < other.to_timestamp()

    def __le__(self, other):
        return self.to_timestamp() <= other.to_timestamp()

    def __eq__(self, other):
        return self.to_timestamp() == other.to_timestamp()

    def __ne__(self, other):
        return self.to_timestamp() != other.to_timestamp()

    def __gt__(self, other):
        return self.to_timestamp() > other.to_timestamp()

    def __ge__(self, other):
        return self.to_timestamp() >= other.to_timestamp()

    def __str__(self):
        if self.__date:
            return self.__date
        else:
            return 'None'