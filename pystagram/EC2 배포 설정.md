# EC2 배포 설정

### Local 설정

vi 명령어로 접근 후 아래처럼 작성합니다.
```shell
sudo vi /etc/default/locale
```

```
LC_CTYPE="en_US.UTF-8"
LC_ALL="en_US.UTF-8"
LANG="en_US.UTF-8"
```

### Zsh 설정

```shell
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install python3-pip
sudo apt-get install zsh
sudo curl -L http://install.ohmyz.sh | sh
sudo chsh ubuntu -s /usr/bin/zsh
```

### Pyenv 설정
```shell
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils libpq-dev python3-dev liblzma-dev
curl https://pyenv.run | bash
```

vi를 통해 ~/.zshrc 파일을 열어서 아래 내용을 추가한다.
```shell
sudo vi ~/.zshrc
```

```
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

```shell
source ~/.zshrc
pyenv --version
```

```shell
pyenv install 3.12.1
pyenv virtualenv 3.12.1 pystagram
```

```shell
sudo apt-get install python3-setuptools
```

버전 확인
```shell
pyenv --version
```

### github RSA 연동
```shell
ssh-keygen -t rsa -b 4096 -C "your@email.com"
eval "$(ssh-agent -s)"
```

vi로 접속후 다음 내용 작성
```shell
sudo vi ~/.ssh/config
```

```
Host github.com
        AddKeysToAgent yes
        IdentityFile ~/.ssh/id_rsa
```

```shell
ssh-add -k ~/.ssh/id_rsa
```

vi로 접속하여 이메일 전까지 == 두개 있는 부분까지 복사 후 github 설정에 추가
```shell
sudo vi ~/.ssh/id_rsa.pub
```


```shell
git clone git@github.com:본인계정/본인프로젝트.git
```

```shell
pyenv virtualenv 3.12.1 pystagram
pyenv local pystagram
python --version
```

```shell
curl -sSL https://install.python-poetry.org | python -
```

vi로 접속하여 맨 밑에 다음 내용 추가
```shell
vi ~/.zshrc
```

```shell
export PATH="/home/ubuntu/.local/bin:$PATH"
```

```shell
source ~/.zshrc
cd ..
cd pystagram
poetry --version
```


```shell
poetry install
python manage.py runserver
```

vi로 접속하여 본인 secret.json 내용 추가
```shell
mkdir .config_secret
cd .config_secret
vi secret.json
```


```shell
cd ..
python manage.py runserver
```
