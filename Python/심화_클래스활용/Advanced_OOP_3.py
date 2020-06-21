
# 출처 : README.md 참조

class Person(object):

    def __init__(self, year, month, day, sex):

        self.year  = year
        self.month = month
        self.day   = day
        self.sex   = sex

    def __str__(self):

        return '{}년 {}월 {}일생 {}'.format(self.year, self.month, self.day, self.sex)


Jun = Person(1988, 7, 4, '남성')
print(Jun)