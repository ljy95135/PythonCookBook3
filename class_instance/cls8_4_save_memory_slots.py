# __slots__ will give instance a more tight/compact representation
# array with static size instead of dict for every instance
# can't add more attributes
# can't multi inherit


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 428B to 156B
