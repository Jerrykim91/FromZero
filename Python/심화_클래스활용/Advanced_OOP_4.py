
# 출처 : README.md 참조

"""
클래스 메소드의 사용법
# 주민등록번호를 인자로 받아 인스턴스를 생성
"""

class Person(object):

    def __init__(self, year, month, day, sex):

        self.year  = year
        self.month = month
        self.day   = day
        self.sex   = sex

    def __str__(self):

        return '{}년 {}월 {}일생 {}'.format(self.year, self.month, self.day, self.sex)


ssn_1 = '900829-1000006'
ssn_2 = '951224-2000069'
ssn_3 = '201214-4000069'

def ssnParser(ssn):

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

    return year, month, day, sex


Jun  = Person(*ssnParser(ssn_1))
Jain = Person(*ssnParser(ssn_2))
Rose = Person(*ssnParser(ssn_3))


print(Jun)
print(Jain)
print(Rose)