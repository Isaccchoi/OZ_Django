# 텍스트

- CharField: 짧은 글 / 길이 제한 O
- TextField: 긴글 / 길이 제한 X
- URLField: URL 저장 / CharField
- SlugFIeld: Slug저장 / CharField / 잘 안씀
- UUIDFIeld: UUID 저장 / 잘 안씀

# 파일

- EmailField: 이메일을 저장 
- FileField: 파일 저장
- ImageField: 이미지 저장

# 숫자

- IntegerField: 숫자 필드
- PositiveIntegerField: 양수만 가능함
- BigIntegerField: 큰 숫자 필드 
- PositiveBigIntegerFIeld: 양수만 가능한 큰 숫자필드
- DecimalFIeld: Decimal 저장
- FloatField: Float 저장

# 날짜 시간

- DateTimeField: 날짜 및 시간을 저장
- DateField: 날짜만 저장 
- TimeField: 시간만 저장 

# 연결

- Foreignkey: 1:N관계 / 내가 N
- ManyToManyFIeld: N:N관계
- OneToOneField: 1:1 관계

# 기타

- JSONField: JSON형태의 데이터를 저장













# DB 설계를 잘하는 법

제일 중요한 것은 중복된 데이터를 많이 적지 않습니다.
Join을 과하게 많이하지 않습니다. 



```python
class 포스트:
  글
  이미지들 
  유저
  좋아요카운트: integer => 좋아요 갯수
  
class 유저:
  이메일
  패스워드
  
  
class 좋아요:
  포스트
  유저 
  

  
포스트 1번 => 좋아요를 100개받았구나

누군가 좋아요를 누르면 포스트에 +1을 하고 좋아요 테이블 저장
좋아요를 취소를 하면 포스트에 -1을하고 좋아요 테이블에서 삭제
```



