# Question_01.py 
# 실습 


print('-'*40)
## 연습문제1:아파트에서 소음이 가장 심한 층수를 출력하기
txt = '''국립환경과학원에서는 아파트에서 소음이 가장 심한 층수를 구하는 계산식을 발표했습니다. 소음이 가장 심한 층은 0.2467 * 도로와의 거리(m) + 4.159입니다. 다음 소스 코드를 완성하여 소음이 가장 심한 층수가 출력되게 만드세요. 단, 층수를 출력할 때는 소수점 이하 자리는 버립니다(정수로 출력).
도로와의 거리: 12m '''
print(txt)
#0.2467 * 12(m) + 4.159
print(0.2467 * 12 + 4.159,' 정수 값= ',int(0.2467 * 12 + 4.159))
print('-'*40)

## 연습문제2: 스킬 공격력 출력하기
txt ='''L이라는 게임에서 '왜곡' 이라는 스킬이 AP * 0.6+ 225의 피해를 줍니다. 
이게임에서 AP(Ability power, 주문력)는 마법능력치를 뜻합니다. 
다음 소스 코드를 완성하여 스킹릐 피해량이 출력되게 만드세요 
AP : 102'''
print(txt)

print(102 * 0.6+ 225)
print('-'*40)

##  연습문제3: 정수3개를 입력 받고 합계를 출력하시오
txt ="""다음 소스 코드를 완성하여 정수 세개를 입력받고 합계가 출력되게 만드시오      
(입력)  -10, 20, 30"""
print(txt)

a,b,c = map(int, input('숫자 세가지 입력:').split(','))
print(a+b+c)
print('-'*40)


##  연습문제4: 다음 소스 코드를 완성하여 50, 100, None 출력하시오
txt ="""다음 소스 코드를 완성하여 50, 100, None 출력되게 만드시오      
(표준출력) 50, 100, None """
print(txt)

a,b,c = 50 ,100, None
print(a,b,c)
print(a)
print(b)
print(c)
print( a,'\n', b ,'\n',c)

print('-'*40)


##  연습문제5: 평균점수를 출력하는 프로그램을 만드세요
txt ='''표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 
평균점수를 출력하는 프로그램을 만드세요.
(input에서 안내 문자열은 출력하지 않아야 합니다.) 
단, 평균 점수를 출력할때는 소수점 이하자리는 버립니다.
(정수로 출력)'''
print(txt)

Korean, English, Math, Science = map(int, input().split())
print('check point : ',Korean, English, Math, Science)
avg = (Korean + English + Math + Science )/ 4 
print(' avg : ',int(avg))
# print(int(Korean, English, Math, Science / 4 ))

print('-'*40)

##  연습문제6: 다음 소스 코드를 완성하여 날짜와 시간을 출력되게 만드시오
txt="""
< 입력 >      
year   = 2000     
month  = 10     
day    = 27    
hour   = 11    
minute = 43    
second = 59   
    
print(year,month,day, ---(1)--- )   
print(hour,minute,second, ---(2)--- )   

< 출력 >   
>>> 2000 / 10/27 11:43:59
"""
print(txt)

year   = 2000     
month  = 10     
day    = 27    
hour   = 11    
minute = 43    
second = 59   


print( year, month, day ,sep = '/', end = ' ')
print(hour,minute,second, sep = ':')   
print( year, month, day ,sep = '/')
print(hour,minute,second, sep = ':')   

print('-'*40)

##  연습문제7: 합격 여부 출력
txt='''국어, 영어, 수학, 과학 점수가 있을때 
한 과목이라도 50점 미만이면 불합격이라고 정했습니다. 
다음 코드를 완성하여 합격이면 True,
불합격이면 False가 출력되게 만드세요.
< 입력 >       
Korean = 92    
English = 47    
Math = 86     
Science = 81    
    
print(---(1)--- )   

< 출력 >   

``` >>> False ```
'''
print(txt)
# 한과목이라도 50점 미만이면 불합격 
Korean = 92    
English = 47    
Math = 86     
Science = 50  

print(Science >= 50)
# 한과목이라도 50점 미만이면 불합격  =  50점 이상이면 합격이라는 말 
test = Korean >= 50 and English >= 50 and Math >= 50 and Science >= 50
print(test)

print('-'*40)

##  연습문제8 : 합격여부 구하기
txt="""표준 입력은 국,영,수,과 점수가 입력됩니다. 
국어는 90점 이상 영어는 80점 초과, 수학은 85점 초과, 
과학은 80점 이상일때 합격이라고 정함 
(한과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 
불합격이면 False가 출력되게 만드세요
(input에서 안내 문자열은 출력하지 않아도 된다.)

<표준 입력>     
1. 90 81 86 80 >> Ture     
2. 90 80 85 80 >> False 
"""
print(txt)




print('-'*40)
##   연습문제9 : range로 리스트 만들기-1
txt = """
다음 소스 코드를 완성하여 리스트 
[5, 3, 1, -1, -3, -5, -7, -9]가 출력되게 만드세요. 
리스트를 만들 때는 range를 사용해야 합니다.
< 입력 >       
a = 문법    
print(a)    

< 출력 >   
>>> [5, 3, 1, -1, -3, -5, -7, -9]

"""
print(txt)






print('-'*40)
##   연습문제10 : range로 리스트 만들기-2
txt = """
표준 입력은 정수가  입력됩니다. 
시작숫자는 -10, 끝나는 숫자는 10 입력된 정수만큼 증가하는 
숫자가 들어가도록 튜플을 만들고, 
해당 튜플을 출력하는 프로그램을 만드세요 
(input에서 안내 문자열은 제외)
<표준 입력>     
1. 2    
2. 3     
<표준 출력>     
1. (-10,-8,-6,-4,-2,0,2,4,6,8)       
2. (-10,-7,-4,-1,2,5,8) 
"""

print(txt)






print('-'*40)


print('-'*40)
##  연습문제11 : 최근 3년간 인구 출력하기
txt = """
리스트 year에 연도, population에 
서울시 인구수가 저장되어 있습니다. 
다음 소스 코드를 완성하여 최근 3년간 연도와 인구수가 
리스트로 출력되게 만드세요.
<표준 입력>     
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
 
print()
print()   
<표준 출력>     
[2016, 2017, 2018]
[9930616, 9857426, 9838892]
"""
print(txt)


year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
 

a = population[-3:]
b = year[-3:]
print( b, a )

print('-'*40)
##  연습문제12: 인덱스가 홀수인 요소 출력하기
txt = """
다음 소스 코드를 완성하여 튜플 n에서 인덱스가 홀수인 요소들이 출력되게 만드세요.

<표준 입력>     
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print()   

<표준 출력>     
(75, -10, 32, -15, 76, 2)
"""
print(txt)


n = [-32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2]
n = tuple(n)
# print(n[1:len(n):2])
# print(len(n) )
tmp = (len(n)-1)/2 #  길이를 홀수로 만든다 =>  맨뒤 숫자가 삭제됨 우리는 살려야함 
print(n[1:len(n):2])
print('-'*40)


# 심사문제 2문제 => https://dojang.io/mod/quiz/view.php?id=2212
##  연습문제13: -
txt = """

<표준 입력>     
- 

<표준 출력>     
-
"""
print(txt)
print('-'*40)


##  연습문제14: -
txt = """

<표준 입력>     
- 

<표준 출력>     
-
"""
print(txt)
print('-'*40)


##  연습문제15: 딕셔너리에 게임 캐릭터 능력치 저장하기
txt = """
다음 소스 코드를 완성하여 
게임 캐릭터의 체력(health)과 이동 속도(movement speed)가 
출력되게 만드세요.
<표준 입력>     
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print()
print()

<표준 출력>     
575.6
340

"""
print(txt)
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(camille['health'])
print(camille['movement_speed'])
print('-'*40)

##  연습문제16: -
txt = """

<표준 입력>     
- 

<표준 출력>     
-
"""
print(txt)
print('-'*40)

##  연습문제17: -
txt = """

<표준 입력>     
- 

<표준 출력>     
-
"""
print(txt)
print('-'*40)

##  연습문제18: -
txt = """

<표준 입력>     
- 

<표준 출력>     
-
"""
print(txt)
print('-'*40)