# Unit_07.py
# 출력 방법 알아보기

# sep로 값 사이에 문자 넣기 (공백 ,콤마, 줄바꿈 ,문자 다 ok )
# sep는 구분자라는 의미 
print(100,250, sep = 'x')
print('1\n2\n3')
print('-'*40)

txt = """
- 제어 문자 
    \n : 다음줄로 이동 하며 개행이라고 부름  
    \t : 탭문자, 키보드의  탭과 같음 
    \\ : \를 사용하려면 두번 !!      
"""

print(txt)
print('-'*40)

# 프린트의 다양한 사용 방법 
#print(vla , sep , end)

x = 10 
#del x 
tx = """
NameError 발생
Traceback (most recent call last)
 in ()
      1 x = 10
      2 del x
----> 3 print(x)

NameError: name 'x' is not defined
"""
print(tx)
#print(x)

print('-'*40)

tx = """
# Q&A 
-    변수에 값이 어떻게 저장되나요? 
    - 파이썬은 값 자체도 객체 
        => 그래서 변수에 값을 그대로 저장하지 않고 객체를 가르키는 방식을 사용
        => 예를 들어 다음과 같이 x, y에 1000을 할당 했다면 x, y는 단지 1000이라는 객체를 가르킴 
- 행렬 곱셈 연산자는 numpy모듈설치후 사용 
- $ pip install numpy 
"""
print(tx)

print('-'*40)


# import sys
# print(sys.getrefcount(1000)) 
# # 2: 윈도우에서 처음 레퍼런스 카운트는 2
# # 3: 리눅스에서 처음 레퍼런스 카운트는 3
# x = 1000 
# # x에 1000을 저장
# print(sys.getrefcount(1000))    
# # 3: 1000을 한 번 사용하여 레퍼런스 카운트 1 증가(Windows)
# # 4: 리눅스
# y = 1000  
# # y에 1000을 저장
# print(sys.getrefcount(1000))   
# # 4: 1000을 한 번 사용하여 레퍼런스 카운트 1 증가(Windows)
# # 5: 리눅스
# print(x is y)    
# # True: x와 y가 같은 객체를 가리키고 있으므로 True가 나옴
