







############################################################

# 39


# def hello():
#     print('start')
#     print('hello')
#     print('end')
 
# def world():
#     print('start')
#     print('world')
#     print('end')
 
# hello()
# world()




############################################################

# 38

# def RandomNum(x):
    
#     import random 
#     tmp = list(range(1,46))
#     random.shuffle(tmp)
#     # print('log1')
#     x = int(x)
#     cnt = 0
#     number = []
    
#     for num in tmp:
#         cnt += 1 
#         # print('log2')
#         if cnt <= x : 
#             # print(num)
#             number.append(num)
#             pass

#     number = [num for num in tmp (cnt += 1 if cnt <= x)]
#     # print('Count : %s' % len(number), number)
#     # print('Count : %s' % len(number))
#     return number

# # rang = 1
# print(rang < 100)

############################################################

# 37
# def RandomNum(x):
    
#     import random 
#     tmp = list(range(1,46))
#     # try:
        
#     # except Exception as e :
#     #     print('범위를 벗어났습니다 1 - 45 까지만 가능합니다.', e)

#     random.shuffle(tmp)
#     # print('log1')
#     x = int(x)
#     cnt = 0
#     number = list()
    
#     for num in tmp:
#         cnt += 1 
#         # print('log2')
#         if cnt <= x : 
#             # print(num)
#             number.append(num)
#             pass

#     # print('Count : %s' % len(number), number)
#     # print('Count : %s' % len(number))
#     return number


# # print(findnum)

# def Checker( rang=6 ):

#     myLotto = [ i for i in map(int, input('1-45까지 6개의 숫자를 입력하세요 : ').split())]
#     # print(myLotto)
#     if len(myLotto) != rang:
#         raise Exception(f'{len(myLotto)} 는 6 개') 

#     elif len(set(myLotto))!= rang:
#         raise Exception(f' 값이 중복 됩니다.')

#     LottoWinningNumber = sorted(RandomNum(int(rang)))
#     # print(findnum)
#     c = 0
#     dum = []
#     for i in myLotto :

#         if i in LottoWinningNumber:
#             c += 1
#             print(f"{c}개 맞았습니다.")

#         else:
#             dum.append(i)
    
#     print(f'{c}개 맞았습니다. {sorted(dum)} not in {LottoWinningNumber}') 
        
# try:
#     Checker()

# except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 실행됨
#     print('스크립트 파일에서 예외가 발생했습니다.', e)

############################################################

# 36

# # 올바른 값을 넣지 않으면 에러를 발생시키고 적당한 문구를 표시
# def checker( list , index):

#     if mine not in allowed:
#         raise Exception('잘못된 값을 넣었습니다!') 
#         print(mine)

#     if yours not in allowed:   
#         raise Exception('잘못된 값을 넣었습니다!') 
#         print(yours)

# try:
#     rsp('가위', '바')  # 함수를 try문 안에 집어 넣음 

# except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 실행됨
#     print('스크립트 파일에서 예외가 발생했습니다.', e)



# def idx_print(list, index):
# 	"""
# 	list 와 index를 입력받아야함 
# 	"""
# 	try:
# 		print(list.pop(index))
# 	except IndexError:
# 		print(f'{index} : index의 값을 가져올 수 없습니다.')

# idx_print([1,2,3], 1 )
# idx_print([1,2,3], 10 )	  # index 길이 초과 
# 						# -> 10 : index의 값을 가져올 수 없습니다.


############################################################

# 38

# # 190이 넘는 학생을 발견하면 반복을 종료
# classRoom  = {'1반' : [150, 156, 179, 191, 199], '2반' : [150, 195, 179, 191, 199]}

# try:
#     for class_number, students in classRoom.items():
#         for student in students:
#             if student > 190:
#                 print(class_number, '190을 넘는 학생이 있습니다.')
#                 # break # 바로 상위 for문은 종료되지만 최고 상위 for문은 종료되지 않는다.
#                 raise StopIteration
#                 # 예외가 try 문 안에 있지 않으면 에러 발생시 프로그램이 멈춘다.
# except StopIteration:
#     print('정상종료')  

############################################################

# 37

# # Try & Except
# def index_print(list, index):

#     try:
#         print(list.pop(index))
#     except IndexError:
#         print('{} index의 값을 가져올 수 없습니다.'.format(index))

# index_print([1,2,3], 5) # 5 index의 값을 가져올 수 없습니다.

# # if 문
# def index_print(list, index):
#     if index < len(list):
#         print(list.pop(index))
#     else:
#         print('{} index의 값을 가져올 수 없습니다.'.format(index))

# index_print([1,2,3], 5) # 5 index의 값을 가져올 수 없습니다.


############################################################

# 36

# y = [10, 20, 30]
 
# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요 : ').split())
#     print(y[index] / x)

# # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
# except ZeroDivisionError as err :    
#     print('숫자를 0으로 나눌 수 없습니다.', err)

# # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
# except IndexError as err:           
#     print('잘못된 인덱스입니다.', err)

# except ValueError as err:           
#     print('벗어난 범위 입니다.', err)

############################################################

# 35

# y = [10, 20, 30]
 
# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요 : ').split())
#     print(y[index] / x)

# # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
# except ZeroDivisionError:    
#     print('숫자를 0으로 나눌 수 없습니다.')

# # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
# except IndexError:           
#     print('잘못된 인덱스입니다.')

# except ValueError:           
#     print('벗어난 범위 입니다.')

############################################################

# 34


# try:
#     num = int(input('숫자만!:'))
#     print(f'{num}는 숫자입니다.')


# except:    # 예외가 발생했을 때 실행됨
#     print('숫자가 아닙니다.예외가 발생했습니다.')

############################################################

# 33

# from abc import *
 
# class CookBase(metaclass=ABCMeta):
#     """
#     반드시 해야 하는 일을 추상메소드로 구현 
#     """
#     @abstractmethod
#     def FindRecipe(self):
#         pass
 
#     @abstractmethod
#     def Ingredients(self):
#         pass
 
# class Cook(CookBase):
#     """
#     구현할때 Base에서 구현한 item(@abstractmethod 추상메소드)은
#     자식클래스에서 모두 구현 해야한다 - 아니면 에러발생 
#     """
#     def FindRecipe(self):
#         print('요리 레시피 준비')
 
#     def Ingredients(self):
#         print('요리재료 준비')
 
# james = Cook()
# james.FindRecipe()
# james.Ingredients()



############################################################

# 32

# class Father:
    
#     def __init__(self):
#         self.fname = '김우빈'

#     def fatherName(self):
#         print(f'아빠는 {self.fname} ,')

# class Mather:

#     def __init__(self):
#         self.mname = '신민아'

#     def matherName(self):
#         print(f'엄마는 {self.mname} ,')

# class Child(Father,Mather):

#     def __init__(self):
#         # super().__init__()
#         Father.__init__(self)
#         Mather.__init__(self)
#         self.name = '김빈아'

#     def greeting(self):
#         super().__init__()
#         print(f'저는 {self.name}입니다.')

# child = Child()
# print(child.__dict__)

# child.fatherName()
# child.matherName()
# child.greeting()

############################################################

# 31

# class Person:

#     def __init__(self):
#         print('부모 - 생성자')
#         self.hello = '안녕하세요!'
 
# class Doctor(Person):

#     def __init__(self):
#         print('자식 - 생성자')
#         super().__init__()              # super()로 부모 __init__  호출
#         self.hospital = 'Severance!'


# Joy = Doctor()
# print(Joy.hello)  
# print(Joy.hospital)  

############################################################

# 30 - 미완

# class Person:

#     def greeting(self):
#         print('안녕하세요!')
 
# class PatientChart(Person):
#     """
#     Person을 상속 받음
#     """
#     def __init__(self):

#         self.patient_chart = []  # Person 인스턴스를 담을 그릇

#     def appendPatient(self, preson):

#         self.patient_chart.append(preson)
#         return self.patient_chart
        


# Joy = PatientChart()
# Joy.greeting()     
# Joy.appendPatient('k')
# # print(Joy())
# print(Joy)  

############################################################

# 29

# class Person:

#     def greeting(self):
#         print('안녕하세요!')
 
# class Doctor(Person):
#     """
#     Person을 상속 받음
#     """
#     def checkUp(self):
#         print('어디가 아프신가요?')


# Joy = Doctor()
# Joy.greeting()     
# Joy.checkUp()       

############################################################

# 28

# class Mall:
#     """
#     wMart와 eMart 중 어디가 더 저렴할까 ?
#     """

#     @staticmethod
#     def wMart(a, b):
#         print(f'$ {int((a + b)*0.8)}')
 
#     @staticmethod
#     def eMart(a, b):
#         print(f'$ {a + b}')

# apple = 10 
# soup = 20

# Mall.wMart(apple, soup)    
# Mall.eMart(apple, soup)    # 클래스 -> 바로 메서드 호출

############################################################

# 27

# class creditCard:
#     """
#     1만불 한도의 신용카드 
#     """
#     __money_limit = 10000    # 비공개 클래스 속성
 
#     def  show_money_limit(self):
#         print(creditCard.__money_limit)    # 내부 접근
 
 
# amax = creditCard()
# amax.show_money_limit()    # 1만불
 
# print(creditCard.__money_limit)    # 외부 접근 불가

############################################################

# 26
# class Person :
#     # bag = [] 
#     def __init__(self):
#         self.bag = []

#     def putBag(self, stuff):
#         self.bag.append(stuff)

# Jerry = Person()
# Jerry.putBag('Books')

# Joy = Person()
# Joy.putBag('wallet')

# print(Jerry.bag) # 제리의 가방
# print(Joy.bag)   # 조이의 가방 

############################################################

# 25

# class Person :
#     bag = [] 

#     def putBag(self, stuff):
#         self.bag.append(stuff)

# Jerry = Person()
# Jerry.putBag('Books')

# Joy = Person()
# Joy.putBag('wallet')

# print(Jerry.bag) # 제리의 가방
# print(Joy.bag)   # 조이의 가방 

############################################################

# 24

# class Person:

#     """
#     매개변수 : self, 이름, 나이, 주소 
#     + 지갑
#     """

#     def __init__(self, name, age, address, wallet):

#         self.hello    = '안녕!'
#         self.name     = name      # self에 넣어서 속성으로 만듦
#         self.age      = age
#         self.address  = address
#         self.__wallet = wallet    #  __를 붙여서 비공개 속성

#     def Greeting(self):
#         # print('{0} 나는 {1}야!'.format(self.hello, self.name))
#         print(f'{self.hello} 나는 {self.name}야!')

#     def pay(self, amount):

#         self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
#         print('잔여 금액 : {0}원'.format(self.__wallet))

# Joy = Person('조이', 30, '인천', 500000 )  # 인스턴스 생성 
# # Joy.__wallet                    # 비공개 속성이라 외부에서 접근 불가능 -> 에러발생 
# Joy.pay(3900)  
# # Joy.Greeting()

############################################################

# 23

# class Person:
#     """
#     매개변수 : self, 이름, 나이, 주소 
#     """

#     def __init__(self, name, age, address):
#         self.hello   = '안녕!'
#         self.name    = name
#         self.age     = age
#         self.address = address

#     def Greeting(self):
#         # print('{0} 나는 {1}야!'.format(self.hello, self.name))
#         print(f'{self.hello} 나는 {self.name}야!')

# Joy = Person('조이', 30, '인천' )
# Joy.Greeting()

# print('이름:', Joy.name)       
# print('나이:', Joy.age)        
# print('주소:', Joy.address)    

############################################################

# 22

# class Person:
#     def greeting(self): # 메소드(Method)
#         print('Hello')

# Jerry = Person()  # 인스턴스(instance)
# Jerry.greeting()

############################################################

# 클래스

############################################################

# 21

# def Factorial(n):
#     if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
#         return None
#     if n == 1:
#         return 1
#     return n * Factorial(n - 1)

# print(Factorial(3))

############################################################

# 20

# def factorial(n):
#     if n == 0:      
#         return  0   
#     return n * factorial(n - 1)    
 
# print(factorial(5))


############################################################

# 19

# def Func(cnt):
#     if cnt == 0:  # 종료 조건을 만듦. 
#                     # cnt가 0이면 다시 Func 함수를 호출하지 않고 끝냄
#         return
    
#     print('Hello, world!', cnt)
    
#     cnt -= 1        # cnt를 1 감소시킨 뒤
#     Func(cnt)       # 다시 Func에 넣음
 
# Func(5)             # Func 함수 호출


############################################################

# 18

# def Closr(tag):  
#     tag = tag  

#     def Func(input):  
#         txt = input  
#         print(f'<{tag}>{txt}<{tag}>')

#     return Func  

# h1Func = Closr('h1')  
# pFunc  = Closr('p')  

# h1Func('h1태그의 내부')  
# pFunc('p태그의 내부')  

############################################################

# 17

# def Closr(tag):  
#     txt = '안녕하세요'  
#     tag = tag  

#     def Func():  
#         print(f'<{tag}>{txt}<{tag}>')

#     return Func  

# h1Func = Closr('h1')  
# pFunc  = Closr('p')  

# h1Func() 
# pFunc()  

############################################################

# 16

# def Func():
#     Code = 'Func의 test'

#     def FuncInFunc():
#         print(Code)
        
#     return FuncInFunc

# MyFunc = Func()

# d = [dir(MyFunc),
#     type(MyFunc.__closure__),
#     MyFunc.__closure__, 
#     MyFunc.__closure__[0],
#     dir(MyFunc.__closure__[0]),
#     MyFunc.__closure__[0].cell_contents
#     ]

# for i in d :
#     print(i)
#     print('='*50)

############################################################

# 15

# def outer_func(): #1
#     message = 'Hi' #3

#     def inner_func(): #4
#         print(message) #6

#     return inner_func #5

# my_func = outer_func() #2

# print(my_func)

############################################################

# 14

# 연습 문제 

# def cnt():
#     i = 0 
#     def count(x):
#         nonlocal i
#         i = i + 1
#         print(i)
#     return count

# c = cnt()
# for i in range(10):
#     c(i)

# print('='*50)

# def cnt_an():
#     i = 0 
#     def count_an(x):
#         nonlocal i
#         i += 1
#         return i 
#     return count_an

# my_fnc = cnt_an()
# for k in range(10):
#     print(my_fnc(k), end= ' ')

############################################################

# 13

# def calc():
#     a = 3
#     b = 5
#     total = 0
#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#     return mul_add
 
# c = calc()
# c(1)
# c(2)
# c(3)

############################################################

# 12

# def closr():                
#     i = 10
#     j = 10
#     tal = 0

#     def mul(x):   
#         nonlocal tal
#         tal = tal + i * x + j       
#         print(tal)  
#     return mul

# y = closr() 
# # print(y(1))
# # print(y(1),y(2),y(3))
# y(1)
# y(2)
# y(3)

# # Output
# # >>> 20
# # >>> 50
# # >>> 90
# # >>> None None None

############################################################

# 11

# # lambda 사용 

# def closr():                
#     i = 10
#     j = 10

#     return lambda x: i * x + j  # 람다 표현식을 반환 

# y = closr() 
# print(y(1),y(2),y(3),y(4),y(5))

# # Output
# # >>> [20, 30, 40, 50, 60]

############################################################

# 10

# nonlocal를 사용하는 이유 
# def outer():
#     a = 10
#     def inner():
#         a += 10
#         print('a:', a)
#     inner()
# outer()

# Output
# >>> UnboundLocalError: local variable 'a' referenced before assignment


# def outer():
#     a = 10
#     def inner():
#         nonlocal a
#         a += 10
#         print('a:', a)
#     inner()
# outer()

############################################################

# 9

# ## 클로저 형태의 함수 

# def closr(): # 1. 선언 
#     i = 10
#     j = 10

#     def mul(x):            # 4. 호출
#         return i * x + j   # 5. 함수 밖의 변수 호출해서 연산 후 리턴  

#     return mul             # 3. mul 함수자체를 반환 -> ()는 사용하면 x 

# y = closr() # 2. 호출 
# print(y(1),y(2),y(3),y(4),y(5))

# # Output
# # >>> 20 30 40 50 60 

# dum = [ y(i) for i in range(1,6)]
# print(dum) 

# # Output
# # >>> [20, 30, 40, 50, 60]

############################################################

# 8

# # global a
# a = 1
 
# def test():
#     # global a
#     a = 3
#     b = 2
 
#     return a + b
 
 
# print('>>> test\n',test())
# print('>>> a\n',a)

############################################################

# 7

## global변수 사용 

# x = 1 
# def Fst_Phase():
#     x = 50         # Fst_Phase의 지역변수 x
#     def Fst_Part():
#         x = 70     # Fst_Part의 지역변수 x
#         def Fst_Step():
#             global x
#             x = x + 80
#             print(x)

#         Fst_Step()

#     Fst_Part()

# Fst_Phase()


# # Output

############################################################

# 6
# def Outer():
#     x = 35        # 지역변수 x
#     def Inner():
#         nonlocal x
#         x = 25    
#     Inner()
#     print(x)      # 지역변수 출력 

# Outer() 

############################################################

# 5
# def Outer():
#     x = 35        # 지역변수 x
#     def Inner():
#         x = 25    
#     Inner()
#     print(x)      # 지역변수 출력 

# Outer()

############################################################

# 4
# def Func():
#     Code = 'Func의 test'

#     def FuncInFunc():
#         print(Code)
        
#     FuncInFunc()

# Func()

############################################################

# # 3
# def Func():
#     Code = 'Func의 test'

#     def FuncInFunc():
#         print(Code)
        
#     return FuncInFunc()

# Func()

############################################################

# 2

# x = 100  
# def val():
#     x = 10
#     print(x) # 전역변수 

# val()
# print(x)

############################################################

# 1 

# x = 100  # 전역 변수 
# def val():
#     print(x) # 전역변수 

# val()
# print(x)

############################################################