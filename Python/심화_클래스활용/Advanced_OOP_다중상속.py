
# 출처 : README.md 참조

# 다중 상속 실습 
# https://uzooin.tistory.com/137


class Father:
    
    def __init__(self):
        self.fname = '김우빈'

    def fatherName(self):
        print(f'아빠는 {self.fname} ,')

    def func(self):
        print('call Father.func')


class Mather:

    def __init__(self):
        self.mname = '신민아'

    def matherName(self):
        print(f'엄마는 {self.mname} ,')

    def func(self):
        """
        다중 상속 - need
        """
        print('call Mather.func')


class Child(Father, Mather):

    def __init__(self):
        # super().__init__()
        Father.__init__(self)
        Mather.__init__(self)
        self.name = '김빈아'

    def greeting(self):
        super().__init__()
        print(f'저는 {self.name}입니다.')

    def oneFunc(self):
        Father.func(self)


    def twoFunc(self):
        Mather.func(self)



child = Child()

print(child.__dict__)

child.fatherName()
child.matherName()
child.greeting()

# 메소드가 사용되어 질때 첫번째 메소드부터 순차적으로 검색

child.oneFunc()
child.twoFunc()