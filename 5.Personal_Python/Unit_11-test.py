# 사용자 함수 
from fun_pkg.random_num import random_num # 랜덤 숫자 생성

# Unit_11-test.py
# 시퀸즈 자료형 활용하기 - 응용 연습 

txt = """
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
print(txt)
print('-'*40)


# 시퀸즈 객체 반복 
a = [[1,2,3]] * 5 
b = [1,2,3] * 5

print(b)
print('-'*40)

test = [1] * 5
test_1 = [[0]] * 10 
print(test)
print(test_1)

print('-'*40)

tmp = list()
for i in range(1,10):
    # print(i)
    # tmp.append(i)
    tmp.append([i])

print(tmp)
print('-'*40)


# 리스트 내포 
tmp1 = [[i] for i in range(1,10)]
print(tmp1)

print('-'*40)



# 요소에 값 할당하기 
"""
- 시퀸즈 객체[인텍스] = 값

"""
a = [0]*5 
print(a)
for i in range(len(a)) : 
    print('a[%d] = ' % i, a[i])
    # print(i)

# 변경 
a = [0]*5 
b = random_num(5)
# print(b)
for i in range(len(b)) : 
    print('b[%d] = ' % i, b[i])

tmp = []
zro = [0] * 5 
rdm_num = random_num(5)
print('rdm_num :',rdm_num)
# print(zro)
for i in range(len(zro)) : 
    # print('zro[%d] = ' % i, zro[i])
    print(i)

    for j in range(len(rdm_num)):
        # print(rdm_num)
        # dum = 0
        pass
        # print('test : rdm_num[%d] = ' % i, rdm_num[i])
        # print('정상작동')
    zro[i] = rdm_num[i]
    print('rdm_num[%d] = ' % i, rdm_num[i])
    tmp.append(zro[i])

print('zro[i]만 추출',tmp)
print(tmp[0])
print(tmp[4])