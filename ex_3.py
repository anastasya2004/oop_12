class User:
    users = []

    def __init__(self, info):
        self.id = info[0]
        self.nick_name = info[1]
        self.firstname = info[2]
        self.last_name = info[3]
        self.middle_name = info[4]
        self.gender = info[5]

    def update(self, id=None, nick_name=None, first_name=None,
               last_name=None, middle_name=None, gender=None):
        if id:
            self.id = id
        if nick_name:
            self.nick_name = nick_name
        if first_name:
            self.firstname = first_name
        if last_name:
            self.last_name = last_name
        if middle_name:
            self.middle_name = middle_name
        if gender:
            self.gender = gender

    def __str__(self):
        output = f'ID: {self.id} Nickname: {self.nick_name} Name: '
        if self.last_name:
            output += f'{self.last_name} '
        output += f'{self.firstname} '
        if self.middle_name:
            output += f'{self.middle_name} '
        if self.gender:
            output += f'Gender: {self.gender}'
        return output


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

class Meeting:
    lst_meeting = []

    def __init__(self, info):
        
        self.id = info[0]
        self.date = info[1]
        self.title = info[2]
        self.employees = []

    def __str__(self):
        output = f'Рабочая встреча {self.count()}\n'
        output += f'{Date(self.date).date} {self.title}\n'
        for pers in self.employees:
            output += f'{pers}\n'
        return output

    @classmethod
    def count_meeting(cls, date):
        counter = 0
        for meet in Meeting.lst_meeting:
            if Date(meet.date) == date:
                counter += 1
        return counter

    @classmethod
    def total(cls):
        counter = 0
        for meet in Meeting.lst_meeting:
            for _ in meet.employees:
                counter += 1
        return counter

    def add_person(self, person):
        self.employees.append(person)

    def count(self):
        return self.id

    @classmethod
    def total(cls):
        counter = 0
        for meet in Meeting.lst_meeting:
            for _ in meet.employees:
                counter += 1
        return counter


class Load:
    @classmethod
    def write(cls, file_name1, file_name2, file_name3):
        with open(file_name1, 'r', encoding='utf-8') as file:
            atributes = file.readline().split(';')
            for line in file.readlines():
                line = line.split(';')
                info = [line[atributes.index('id')],
                        line[atributes.index('date')],
                        line[atributes.index('title')]]
                Meeting.lst_meeting.append(Meeting(info))

        with open(file_name2, 'r', encoding='utf-8') as file:
            for line in file.readlines()[1:]:
                line = line.strip().split(';')[:-1]
                User.users.append(User(line))

        with open(file_name3, 'r', encoding='utf-8') as file:
            atributes = file.readline().split(';')
            for line in file.readlines():
                line = line.split(';')
                info = [line[atributes.index('id_meet')],
                        line[atributes.index('id_pers')]]
                meeting = [meet for meet in Meeting.lst_meeting if meet.id == info[0]]
                person = [man for man in User.users if man.id == info[1]]
                meeting[0].add_person(person[0])