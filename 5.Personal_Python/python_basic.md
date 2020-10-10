
---
### 이터레이터 
    반복 가능한 객체를 말한다 
    객체에 .next가 가능하다면 이터레이터가 맞음 
    list는 반복 가능하지만 이터레이터는 아니다 
    명시적으로 반복가능란 객체로 만들어서 사용해야한다.

- **이터러블** 
    반복 가능하다는 뜻 => 반복(loop)연산이 가능하여 
    해당 위치를 이동해가면서 값을 사용할수 있는지를 말함

    a라는 dict를 생성하여 class 확인을 하면 a는 dict일뿐 이터레이터는 아니다. 

- 이터레이션 
반복가능한 객체에사 해당 값을 가져오는 행위 

- 이터 함수 
    list나 dict를 이터레이터로 만들어 주는 함수
    dict를 생성하여  iter함수를 통하여 b라는 이터레이터를 만듬
    이터러블 하기때문에 for문과 짝을 이루어 사용한다. 


### 제너레이터 
    이터레이터를 만들어주는것을 말함 
    = 반복 가능한 객체를 만들어 주는 행위 

- yield
    function에서 return과 동일한 역할을 수행 = 반환값

```py
# def generator(n):
#     print "get_START"
#     i = 0
#     while i < n:
#         yield i
#         print "yield 이후 %d" % i
#         i += 1
#     print "get_END"

# for i in generator(4):
#     print "for_START %d" % i
#     print i
#     print "for_END %d" % i

```    
<hr />
< 참고 자료 >      
    1. [fastcampus](www.fastcampus.co.kr)    
    2. [A Byte of Python](http://byteofpython-korean.sourceforge.net/byte_of_python.html)    
    3. [codecademy](https://www.codecademy.com/)    
