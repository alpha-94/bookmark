from django.db import models
from django.urls import reverse


# Create your models here.
# 모델 : 데이터베이스를 sql 없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다.
# 모델 = 테이블
# 모델의 필드 = 데이트블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약사항 결정 ( 글자의 크기, 등등)
    # 3. Form 의 종류
    # 4. Form 에서 제약사항

    def __str__(self):
        return '이름 : ' + self.site_name + ' || '+ ' 주소 : ' + self.url


    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

# 모델을 만들었다 -> 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정
# python manage.py makemigrations bookmark
# make migrations -> 모델의 변경사항을 추적해서 기록
# 마이그레이션(migrate) -> 데이터베이스에 모델의 내용을 반영(테이블 생성)

