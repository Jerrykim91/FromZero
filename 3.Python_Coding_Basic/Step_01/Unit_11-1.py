# 사용자 함수 
from fun_pkg.random_num import random_num # 랜덤 숫자 생성

# Unit_11-1.py

# 인덱스 사용하기 
txt_index = """
# 인덱스 사용하기 
    => 시퀸스 객체에 [](대괄호)를 붙이고 []안에 각 요소의 인텍스를 지정하면 해당 요소에 접근가능 
- 시퀸즈 객체에 들어있는 요소에 접근하는 방법을 확인 
- 시퀸즈 객체의 각 요소는 순서는 정해져 있으며 이 순서를 인덱스라고 함 

시퀸스 객체[인덱스]

## 인덱스( index, 색인 )
    - 위칫값을 뜻하는데 국어사전 옆면에 ㄱ, ㄴ, ㄷ으로 표시해 놓은것과 비슷 
    - 주의 ) 시퀸스 객체의 인덱스는 항상 0부터 시작한다는거 


""" 
print(txt_index)
print('-'*40)

# 인덱스 사용하기 - 1 

a = [38,26,53,72,19]
print('-'*20)

print(a[0])   # 리스트의 첫번째 요소를 출력 => 인덱스 0 
print('-'*20)

print(a[2])   # 리스트의 세번째 요소를 출력 => 인덱스 3
print('-'*20)

print(a[4])   # 리스트의 다섯번째 요소를 출력 => 인덱스 4
print('-'*20)

# 튜 플 
b = (38,26,53,72,19)
print(b[2])    # 튜플의 세번째 요소를 출력 => 인덱스 3
print('-'*20)

ran = range(0, 10, 2) # 0 부터 10 까지 2 단계씩 출력 
r = list(ran)

print(ran[2])
print('-'*20)

print( r ) # print(ran[2])가 제대로 출력된 것을 확인가능
print('-'*40)

# 문자열 인덱스 
hello = 'hello world!'

print( hello[2] )
print( hello[5] )   # 공백도 인식
print('-'*20)

hello = list(hello) # 확인 
print(hello)
print('-'*40)

# 시퀸즈 객체에 인덱스를 지정하지 않으면 
# c를 이용해서 확인 
c = [ 38, 26, 53, 72, 19]
print(c) # c를 그냥 불러오는것 => c에 담긴 리스트 내용의 전부를 출력 
print('-'*40)

# __getitem__ 메소드 

txt_getitem = """
#  __getitem__ 메소드
시퀸즈 객체에서 대괄호를 사용하면 
실제로는 __getitem__ 메소드가 호출되어 요소를 가져옴 

직접 호출도 가능 
시퀸스 객체. __getitem__(index)

__getitem__메서드를 이용한 추가적인 것은 
unit_39(이터레이터)에서 추가로 설명  

일단 아래에 __getitem__메서드를 이용해 호출 해보겠음
"""
print(txt_getitem)
print('-'*40)
 
# __getitem__ 메소드 - 실습  
a = list(range(10))
# print( a )
print(a.__getitem__(5))
print('-'*40)

# 음수 인덱스 지정하기 
# 내가 만든 함수로 임의 숫자를 가지고 오는 거임  
ran = random_num(5)
print(ran, ran[-2], ran[-1])
print('-'*40)

# 튜플로 인덱스 지정하기 
ran_1 = tuple(ran)
print(ran_1,ran_1[-3])
print('-'*40)

r = range(1,11,2)
print(r[-2])
print('-'*40)

hello = 'hello world!'
print(hello[-1])
print('-'*40)

# 인덱스의 범위를 벗어 날때 
# 에러 남 => index error : list index out of range
# 리스트의 인덱스가 범위를 벗어나서 에러 발생 

# 마지막 요소에 접근하기 
a = random_num(10)
print(a,'\n 요소 길이 : ', len(a),'\n 마지막요소 : ',a[len(a)-1])
# a[len(a)-1] 이방법은 마지막 인덱스를 구할때 종종 사용 ! 
print('-'*40)

# 요소에 값 할당하기 
"""
- 시퀸즈 객체[인텍스] = 값

"""
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

print('zro[i]만 추출 :', tmp)
print('tmp[0] : ', tmp[0])
print('tmp[4] : ', tmp[4])
print('-'*40)


# del로 요소 삭제하기 
"""
del 시퀸즈 객체[인덱스]
"""

print(tmp) # before
del tmp[2]

print(tmp) # after -> 삭제된것을 확인 할수 있음 
print('-'*40)
