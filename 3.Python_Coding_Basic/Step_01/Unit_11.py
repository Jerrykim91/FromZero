# 사용자 함수 
from fun_pkg.random_num import random_num # 랜덤 숫자 생성

# Unit_11.py
# 시퀸즈 자료형 활용하기

txt_sequence = """
# 시퀸즈 자료형 활용하기 
- 리스트 , 튜플 , range, 문자열 => 연속성(sequence)을 가짐 
- 시퀸즈 자료형 => ( 리스트 , 튜플 , range, 문자열)
- 시퀸즈 자료형의 공통기능 사용 
    - 시퀸스 자료형의 큰 특징을 공통동작과 기능을 제공 
    - 시퀸즈 자료형으로 만든 객체를 시퀴즈 객체라고 함 => 각 값을 요소라고 칭 함 
    - 특정 값을 확인 
        => 값 in 시퀸즈 객체
        => 값 not in 시퀸즈 객체
        => 값 in range(값)
    - 시퀸즈 객채 연결하기 
        - 시퀸즈 객체 1 + 시퀸즈 객체 2  
        - **range는 + , \* 연산자로 객체를 연결 할 수 없다.** 
            - 근데!  리스트, 튜플로 묶어서 연결하면 가능 => 아래 예시 참조
     - 시퀸즈 객체 반복 
         - 시퀸즈 객체 * 정수
         - 정수 * 시퀸즈 객체 
     - 시퀸즈 요소 개수 구하기 
         - len(시퀸즈 객체)
             -> 리스트, 튜플, 문자열도 마찬가지로 길이를 구할 수 있다. 
             - range의 숫자 생성 개수 구하기 =>len(range( 값 ))
"""
print(txt_sequence)
print('-'*40)

# 시퀸즈 객채 연결하기 -> 시퀸즈 객체 1 + 시퀸즈 객체 2  
a  = [1,2,3]
b  = [6,7,8]
print(a + b)
print('-'*40)

# 이렇게
a = list(range(0,5)) + list(range(6,12))
print(a)
print('-'*40)

# 시퀸즈 객체 반복 
b = [1,2,3] *5
print(b)
print('-'*40)

# 시퀸즈 요소 개수 구하기  -> 리스트 튜플도 구해짐 
a  = [1,2,3]
print(len(a))
print('-'*40)

# range의 숫자 생성 개수 구하기 
a = len(range(0,10,2))
print(a)
print('-'*40)

# 문자열 길이 구하기 - 영어 
hello = 'Hello, world!'
print('print_hello_len : ',len(hello))
print('-'*40)

# 문자열 길이 구하기 - 한국어 
hello = '안녕하세요'
print('print_안녕하세요_ 길이 : ',len(hello))
print('-'*40)
