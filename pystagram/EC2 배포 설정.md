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

