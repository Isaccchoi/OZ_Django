

## 설정
```shell
$ cd config
$ ln -sf local.py settings.py
```


### Poetry 추출
```shell
$ poetry export --without-hashes --format=requirements.txt > requirements.txt
```