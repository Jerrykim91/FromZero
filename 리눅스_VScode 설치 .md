<br>

#### 2. Ubuntu 18.04 - VScode 설치 

<br>

# VScode 설치 

아직까지는 이명령어로 에러난적은 없기 때문에 혹시라도 에러사항이 생긴다면 업데이트 하도록 하겠다.

<br>

## 1. VScode 설치 

<br>

필자는 VScode를 굉장히 선호하는편이라 컴퓨터를 세팅할때 가장 VScode 먼저 설치한다. 

<br>

일단은 `curl`을 설치해 준다. 

```bash
# 설치 
$ sudo apt-get install curl
```

<br>

그리고 이후 아래 코드를 입력한다.  

<br>

```bash

# 경로를 복사
$ sudo sh -c 'curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg'

# 경로를 추가 
$ sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

```

<br>

이제 패키지 목록을 불러온 다음 vscode를 설치하면 설치가 완료된다. 

<br>

```bash

# 패키지 목록 불러오기 
$ sudo apt-get update

# vscode 설치
$ sudo apt-get install code

```

이렇게 설치가 완료되었다. 

만약 비쥬얼 코드를 실행하고자 한다면 
커맨드 창에서 `code`치면 실행된다.

<br>

## Git 설치 

만약 VScode에서 깃허브를 이용해야한다면 `git`을 설치해야한다.     
그러기위해서는 아래와 같이 진행하자 ! 

<br>

```bash

# Git 설치 방법

$ sudo apt-get install git    # git 설치 명령어

```

<br>

### 레지스트리를 다운로드 할 경우

주의 할점 : 다운 받고자 하는 경로를 잘 입력해서 올바른 경로에 설치하자 !     
생각없이 설치하다가는 어디있는지 못찾게 된다. 

<br>

```bash

# 레지스트리 다운로드 
$ git clone 레지스트리 경로.git

# 레지스트리 삭제 
$rm -rf ~/레지스트리 이름 

```

<br>
<br>


---

<br>

## Reference <br>

- 내용 &nbsp; : &nbsp;<주소> <br>

<br>
<br>

## Practice makes perfect! <br>

- [내용](주소)