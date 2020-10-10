# Unit_08.py
# 불과 비교 연산자, 논리 연산자 알아보기 

tx = """
# 불과 비교 연산자, 논리 연산자 알아보기 

- Programming을 하다 보면 참과 거짓을 판단해야 할 때가 많음
- Boolean = > 참(True)과 거짓(False)을 나타냄
- 두 값의 관계를 판단하는 **비교 연산자**와 두 값의 논리값을 판단하는 **논리 연산자** 

++ 비교 연산자와 논리 연산자의 판단의 결과 => 참(True)과 거짓(False)     
- 숫자가 같은지 다른지 비교 , 문자열도 마찬가지      
    => 두숫자의 값을 비교 하려면 ==(equal)     
    => 다른지를 비교하려면 !=( not equal)을 사용      
    
++ 객체가 같은지 다른지 비교 => is, is not => **객체를 비교**     
++ 정수 객체와 실수 객체가 다른것을 확인하려면 id()함수를 사용     
- 주로 is, is not은 클래스로 객체를 만든뒤 객체가 서로 같은지 비교 할때 사용      
    - Point는 ==,!= 는 is, is not 과 같은 느낌이나 **동작 방식이 다르다**는 것이 KeyPoint!
    
    
### 논리 연산자 사용하기 
    -> 논리 연산자 (AND, OR , NOT) => 세 연산자가 한식에 들어 있으면 NOT > AND > OR 
AND : A AND B => 두 값이 모두 True => True     
OR  : A  OR B =>두 값 중 하나라도 True => True 이말은 두값이 모드 False => False    
NOT : A NOT B => NOT은 논리 값을 뒤집는다 => 이말인 즉, (NOT True => False , NOT False = True)  
"""
print(tx)
print('-'*40)

# 숫자 
print(10 == 10 , 10 != 10)
# 문자열 
print('python' == 'Python' , 'python' != 'Python')
# 부등호 
print(10 > 20 , 10 < 20 , 10>=10 ,10 <= 10)

# 부등호 잘 헷갈림 ** 주의 **
# 크거나 같은지 , 작거나 같은지 
print(11 >= 10 , 11 <= 10)

# 객체가 같은지 다른지 비교 -> is , is not 
print(1==1.0, 1 is 10 , 1 is not 1.0)

print('-'*40)

