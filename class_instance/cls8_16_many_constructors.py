import time


class Date:
    # classmethod

    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)  # Primary
b = Date.today()  # Alternate


class NewDate(Date):
    pass


c = Date.today()  # Creates an instance of Date (cls=Date)
d = NewDate.today()  # Creates an instance of NewDate (cls=NewDate)
