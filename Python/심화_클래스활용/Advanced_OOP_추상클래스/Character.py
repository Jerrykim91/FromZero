
# 출처 : README.md 참조

# 추상 클래스 실습 - 캐릭터 
# Character.py

from abc import *  # Abstrace Base Class

class Character(metaclass = ABCMeta):

    def __init__(self):
        self.hp = 100
        self.attackPower = 20 

    def attack(self, other, attackKind):
        other.getDamage(self.attackPower, attackKind)

    @abstractclassmethod # Character 클래스를 상속받는 모든 클래스는 함수를 오버라이딩으로 구현해야 인스턴스 생성이 가능
    def getDamage(self, attackPower, attackKind):
        pass


# dev_mode 

if __name__ == '__main__':
    ch1 = Character()

#  Character 클래스를 상속 받아서 Player, Monster 클래스를 각각 정의