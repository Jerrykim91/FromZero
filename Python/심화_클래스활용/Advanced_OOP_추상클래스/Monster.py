
# 출처 : README.md 참조

# 추상 클래스 실습 - 몬스터 
# Monster.py

from Character import Character



# 추상클래스의 자식 클래스(Monster)

class IceMonster(Character):

    def getDamage(self, attackPower, attackKind):

        if attackKind == 'ICE':
            self.hp += attackPower  # +

        else :
            self.hp -= attackPower  # -

    def __str__(self):

        return f"Ice Monster's HP : {self.hp}"


class FireMonster(Character):

    def getDamage(self, attackPower, attackKind):

        if attackKind == 'FIRE':
            self.hp += attackPower  # +

        else :
            self.hp -= attackPower  # -

    def __str__(self):

        return f"Fire Monster's HP : {self.hp}"