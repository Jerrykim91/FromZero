
# 출처 : README.md 참조

# 추상 클래스 실습 - 플레이어 
# Player.py

from Character import Character

# 추상클래스의 자식 클래스(player)
class Player(Character):

    def getDamage(self, attackPower, attackKind):
        self.hp -= attackPower
