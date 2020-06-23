
# 출처 : README.md 참조

# 객체 합성 
# has - a 

class Gun:

    def __init__(self, kind):
        self.kind = kind

    def bang(self):
        print('bang!bang!')
    


# 객체 합성 

class Police():

    def __init__(self, gunKind=''):
        if gunKind:
            self.gun = Gun(gunKind) # Gun클래스의 인스턴스객체 생성
                                    # Police의 인스턴스 멤버로 할당한다. 
        else:
            self.gun = None         # gun이라는 인스턴스 멤버는 존재 but 값은 없음 
    
    def getGun(self, gunKind):
        self.gun = Gun(gunKind)

    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print('당신에게는 총이 없습니다.')



NA_cab = Police('리볼버')
print(NA_cab.gun.kind)  # 리볼버 
NA_cab.shoot()          # shoot it

LA_cab = Police()   
LA_cab.shoot()          # 당신에게는 총이 없습니다. 

LA_cab.getGun('기관총')
LA_cab.shoot()          # shoot it



# 추가 

"""

__name__ = '__main__'

테스트를 위해 넣은 코드가 모듈 import 시에 실행되지 않도록 하는 코드 
python test.py 처럼 직접 파일을 실행시키면 if 문이 참이되어 if 다음 문장들이 수행
모듈을 개발할 때 확인을 위한 테스트 코드 작성시에 활용


# 구조

if __name__ == "__main__":
  ....
  테스트 실행문


# 참조 -> 추후에 리뷰 

https://hashcode.co.kr/questions/3/if-__name__-__main__%EC%9D%80-%EC%99%9C%EC%93%B0%EB%82%98%EC%9A%94

"""

