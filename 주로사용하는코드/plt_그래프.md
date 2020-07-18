<br>

#### 2. 그래프_판다스 - 그래프 


<br>

# 그래프

<br>

## 1. Pie plot

<br>

```py

import matplotlib.pyplot as plt

# 라벨
labels = ('A', 'B', 'C') -> plt.legend(['A','B','C'])
data = [50, 30, 40] 

plt.figure(figsize=(6, 6))

# plt.pie로 생기는 요소를 다음처럼 리턴하여 값을 저장해두고 
patches, texts, autotexts = plt.pie(
    labels=labels,          # 각 이름
    labeldistance=1.1,      # 벌어짐
    x = data,               # 값
    explode=(0.1, 0.1, 0),  # pie가 튀어나오는지 정해줌  
    startangle=90,          # 각도
    shadow=False,           #그림자 
    counterclock=False,     # 시계방향으로 가는지, 시계 반대 방향으로 가는지 정해줌 
    autopct='%1.1f%%',      # pi 위에 표시될 글자 형태, 또한 알아서 %로 변환해서 알려줌 
    pctdistance=0.7,        # pct가 radius 기준으로 어디쯤에 위치할지 정함 
    colors=['grey', 'red', 'blue'],
)


## 도넛처럼 만들기
centre_circle = plt.Circle((0,0),0.50,color='white')
plt.gca().add_artist(centre_circle)

# ## label 색 변경 
# for t in texts:
#     t.set_color("green")
#     t.set_fontproperties(BMDOHYEON)
#     t.set_fontsize(50)

# ## pie 위의 텍스트를 다른 색으로 변경해주기 
# for t in autotexts:
#     t.set_color("white")
#     t.set_fontproperties(BMDOHYEON)
#     t.set_fontsize(20)

plt.tight_layout()
save_path = "../data"
plt.savefig(save_path)
plt.show()

```

<br>




## 2.

<br>

```py

```

<br>



## 3.

<br>

```py

```

<br>



## 4.

<br>

```py

```

<br>





<br>

---

<br>

## Reference <br>

- name &nbsp; : &nbsp;<https://> <br>

<br>
<br>

## Practice makes perfect! <br>

- [내용](주소)