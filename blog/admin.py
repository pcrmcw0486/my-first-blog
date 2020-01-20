from django.contrib import admin
from .models import Post 
#models 에서 Post를 import하고 관리자 페이지에서 만든 모델을 보려면
#admin.site.register(Post)로 모델을 등록해야함.
# Register your models here.
 
admin.site.register(Post)
