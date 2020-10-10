class Man:
    def __init__(self, name):
         self.name = name 
         print("Initialized!")
    
    def hello(self):
        print("HELLO" + self.name + "!")

    def goodbye(self):
        print("Good-bye" + self.name + "!")

m = Man("David") # Man(자기자신, name)
m.hello()
m.goodbye()
# conda activate project



# 2020.02.28 
# 클래스는 또 다른 함수인가 ?  
# 클래스와 생성자가 한 몸이고 
# 생성자가 받아들인 것(파라메터)을 자기 자신이라고 생성자에서 선포하고 
# 그 생성자를 클래스안의 모든 메소드에 인자 값으로 집어 넣는것인가 

# 결국 클래스에서 받아들인 파라메터들은 뿔뿔이 흩어져 
# 각각 사용하고자 하는 함수에 들어가는것인가 ?  
# 틀은 같지만 재료에따라 다르듯 
# 그값을 가졌을대 각기다른 아웃풋이 나오는거고 ?
