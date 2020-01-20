from django.conf import settings
from django.db import models
from django.utils import timezone

#class Post를 설정해준다 python 문법에 익숙해지도록 한다. 속성 값을 그냥 써준다.
#class 첫글자는 대문자로 쓰도록 한다. 
#Post안 models는 Post가 장고 모델임을 의미함으로써 이 코드를 통해 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 된다.
class Post(models.Model):
    #Foreign Key : 다른 모델에 대한 링크 seting의 Auth user model로 연결을 하고 있고, delete시 cascase방식으로 삭제된다(연쇄작용))
    # 모델 필드 및 정의 방법의 사이트는 다음과 같다
    #https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #글자수 제한시 사용 CharField.
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_data = models.DateTimeField(
        default = timezone.now)
    published_data = models.DateTimeField(
        blank = True, null = True
    )

    def publish(self) :
        self.published_data = timezone.now()
        self.save()
    #__ 던더라고 불리는 더블언더스코어의 준말. 파이썬에서 자주 사용됨.
    def __str__(self):
        return self.title

# Create your models here.
