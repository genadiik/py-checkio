from datetime import datetime, date

class Person:
    def __init__(self, first_name, last_name, birth_date,
                 job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        # date_now = datetime.now() # for real life
        date_now = datetime.strptime('01.01.2018', '%d.%m.%Y') # for checkio
        birth_day = (self._birth_date.month, self._birth_date.day)
        now_day = (date_now.month, date_now.day)
        return date_now.year - self._birth_date.year - (now_day < birth_day)

    def work(self):
        if self.gender == 'male':
            return f'He is a {self.job}'
        if self.gender == 'female':
            return f'She is a {self.job}'
        return f'Is a {self.job}'

    def money(self):
        money_val = int(self.working_years * self.salary * 12)
        return f'{money_val:,}'.replace(',', ' ')

    def home(self):
        return f'Lives in {self.city}, {self.country}'

    def __str__(self):
        return f'{self.name()}: \
                \n -- age: {self.age()} \
                \n -- work: {self.work()} \
                \n -- money: {self.money()} \
                \n -- home: {self.home()}'

    @property
    def birth_date(self):
        return self._birth_date.strftime('%d.%m.%Y')

    @birth_date.setter
    def birth_date(self, date_str):
        self._birth_date = datetime.strptime(date_str, '%d.%m.%Y')
