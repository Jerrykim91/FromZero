
# 출처 : README.md 참조

class Person(object):

#    my_class_var = 'sanghee'

    def __init__(self, year, month, day, sex):

        self.year  = year
        self.month = month
        self.day   = day
        self.sex   = sex

    def __str__(self):

        return '{}년 {}월 {}일생 {}'.format(self.year, self.month, self.day, self.sex)


    @classmethod
    def ssnConstructor(cls, ssn):

        front, back = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[:2]

        else :
            year = '20' + front[:2]

        if (int(sex)%2) == 0 :
            sex = '여성'

        else :
            sex = '남성'

        month = front[2:4]
        day   = front[4:6] 

        return cls(year, month, day, sex)

    @staticmethod
    def isWorkDay(day):

        """ 
        근무 여부를 리턴하는 기능을 가진 스태틱 메소드
        월: 0, 화: 1, 수: 2, 목: 3, 금: 4, 토: 5, 일: 6 
        """
        
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True


ssn_1 = '900829-1000006'
ssn_2 = '951224-2000069'
ssn_3 = '201214-4000069'


Jun  = Person.ssnConstructor(ssn_1)
Jain = Person.ssnConstructor(ssn_2)
Rose = Person.ssnConstructor(ssn_3)


print(Jun)
print(Jain)
print(Rose)

import datetime

myDate = datetime.date(2020, 6, 21)
yourDate = datetime.date(2020, 6, 22)


print(Person.isWorkDay(myDate))     # 클래스를 통하여 스태틱 메소드 호출
print(Rose.isWorkDay(myDate))       # 인스턴스를 통하여 스태틱 메소드 호출

print('='*25)

print(Person.isWorkDay(yourDate))
print(Rose.isWorkDay(yourDate))