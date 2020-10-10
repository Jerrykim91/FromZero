
# 출처 : README.md 참조

"""
클래스 메소드의 사용법
"""

class Employee(object):

    raiseAmount = 1.1  # 연봉인상률 클래스 변수 
    numOfEmps   = 0  #1 클래스 변수 정의

    def __init__(self, fst, lst, pay):

        self.first = fst
        self.last  = lst
        self.pay   = pay

        Employee.numOfEmps += 1

    def applyRaise(self):

        self.pay = int(self.pay * self.raiseAmount)

    def fullName(self):

        return '{}{}'.format(self.first, self.last)
    
    def getPay(self):

        return '현재 "{}"의 연봉은 "{}" 입니다.'.format(self.fullName(), self.pay)

    def __del__(self):

        Employee.numOfEmps -= 1   # 퇴사자
       

    @classmethod
    def changeRaiseAmount(cls,amount):

        """
        클래스 메소드 데코레이터를 사용하여 클래스 메소드를 정의 

        인상률이 1보다 작으면 재입력을 요청하는 코드 
        """
        # 데이터 무결성 검사를 실시
        while amount < 1:

            print('[경고] 인상률은 1보다 작을 수 없습니다.')
            amount = input('[입력] 인상률을 다시 입력해 주세요.\n')
            amount = float(amount)

        cls.raiseAmount = amount
        print('"{}" 인상율이 적용 되었습니다.'.format(amount))



emp_1 = Employee('Jerry', 'Kim', 60000)
emp_2 = Employee('Joy', 'Kim', 45000)
emp_3 = Employee('Jain', 'Li', 90000)


# 직원수 

print(f'현재 직원수 : {Employee.numOfEmps}')



# 연봉 인상 전 

print(emp_1.getPay())
print(emp_2.getPay())

# 연봉 인상율 변경
Employee.changeRaiseAmount(0.9) # 재입력 코드 동작 

# 퇴사자 
del emp_3
print('퇴사')

# 연봉 인상

emp_1.applyRaise()
emp_2.applyRaise()


# 연봉 인상 후 

print(emp_1.getPay())
print(emp_2.getPay())

print(f'현재 직원수 : {Employee.numOfEmps}')