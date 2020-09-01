<br>

#### 1. 분석_판다스 -  자주 쓰는 코드정리

<br>

# 자주 쓰는 코드정리

<br>

## 1. 데이터 로드 방법 



<br>

```py

path = './data/COVID_19/%s.csv' 
df = pd.read_csv(path %'PatientInfo')

```

<br>




## 2. 데이터 정보 확인 

<br>

```py

# info 
df.info()

# shape   ->  데이터 길이 (인덱스, 컬럼)
df.shape

# columns ->  컬럼종류
df.columns

```

<br>



## 3. 결측값 확인하는 코드 

<br>

```py

# 데이터 프레임의 전체 널값 확인 
df.isnull().sum()

#  결측치 인 아이만 출력 
df[df.'컬럼이름'.isnull()==True]

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