
# 출처 : README.md 참조

class Employee(object):

    raiseAmount = 1.1  # 연봉 인상률 클래스 변수 

    def __init__(self, fst, lst, pay):

        self.first = fst
        self.last  = lst
        self.pay   = pay
        

    def applyRaise(self):

        """
        직원의 연봉을 인상할때 모든 직원 인스턴스에게 같은 인상율이 적용
        """
        self.pay = int(self.pay * self.raiseAmount)


    def fullName(self):

        return '{}{}'.format(self.first, self.last)
    

    def getPay(self):
        
        return '현재 "{}"의 연봉은 "{}" 입니다.'.format(self.fullName(), self.pay)



emp_1 = Employee('Jerry', 'Kim', 60000)
emp_2 = Employee('Joy', 'Kim', 45000)


# 연봉 인상 전 

print(emp_1.getPay())
print(emp_2.getPay())


# 연봉 인상

emp_1.applyRaise()
emp_2.applyRaise()


# 연봉 인상 후 

print(emp_1.getPay())
print(emp_2.getPay())


# 만약 다음 해에 연봉 인상율을 변경해야 한다면 
# 클래스 메소드를 사용하여 변경하는 것이 좋다.

# 직접 클래스 변수를 변경하는 방법도 있지만 
# 데이터 검사나 다른 부가 기능등의 추가가 필요할때 
# 클래스 메소드를 사용하면 아주 편리하다.