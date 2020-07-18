<br>

#### 1. 그래프_판다스 - 그래프 한글 폰트 설정

<br>

# 그래프 한글 폰트 설정 방법

<br>

## 1. platform을 이용한 폰트 설정 

데이터 먼저 로드하고 해보삼

<br>

```py

# 폰트
import platform

if platform.system() == 'Darwin':    # 맥
    font_name = 'AppleGothic'
elif platform.system() == 'Linux':   # 리눅스
    font_name = 'NanumGothic'
elif platform.system() == 'Windows': # 윈도우
    font_name = 'Malgun Gothic'
else:
    print('알수없는 시스템. 미적용')

plt.rc('font', family=font_name)

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





<br>

---

<br>

## Reference <br>

- name &nbsp; : &nbsp;<https://> <br>

<br>
<br>

## Practice makes perfect! <br>

- [내용](주소)