

# global a
a = 1
 
def test():
    # global a
    a = 3
    b = 2
 
    return a + b
 
 
print('>>> test\n',test())
print('>>> a\n',a)

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