


def factorial(n):
    if n == 1:      
        return 1    # 1을 반환하고 재귀호출을 종료
    return n * factorial(n - 1)    # n *  n - 1을 넣어서 반환된 값을 곱함
 
print(factorial(5))


############################################################

# def Func(cnt):
#     if cnt == 0:  # 종료 조건을 만듦. 
#                     # cnt가 0이면 다시 Func 함수를 호출하지 않고 끝냄
#         return
    
#     print('Hello, world!', cnt)
    
#     cnt -= 1        # cnt를 1 감소시킨 뒤
#     Func(cnt)       # 다시 Func에 넣음
 
# Func(5)             # Func 함수 호출


############################################################

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

# def outer_func(): #1
#     message = 'Hi' #3

#     def inner_func(): #4
#         print(message) #6

#     return inner_func #5

# my_func = outer_func() #2

# print(my_func)

############################################################

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

# ## global변수 사용 

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