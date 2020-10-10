
# 출처 : README.md 참조

# super() 실습 
class father(): 
    """
    부모 클래스
    """

    def __init__(self,  who):

        self.who = who

    def handsome(self):

        print(f'{self.who}를 닮아 잘생겼다')



class Brother(father):
    """
    자식 클래스 - 아들
    """
    pass



class Sister(father):
    """
    자식 클래스 - 딸
    자식클래스(부모클래스) 아빠 메소드를 상속
    """
    def __init__(self,  who, where):

        super().__init__(who)   # super 사용 - 부모(기반)에게 상속
        self.where = where

    def choice(self):
        print(f"{self.where} !!")

    def handsome(self):
        super().handsome()      # super 사용 - 부모(기반)에게 상속
        self.choice()


Girl = Sister("아빠", "얼굴")
Girl.handsome()
