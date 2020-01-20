from django.shortcuts import render
from django.utils import timezone
from .models import Post
# . 은 현재 디렉토리 또는 어플리케이션을 의미.

def post_list(request) : 
    #post에 Post정보를 필터링하여 sorting한다.
    posts = Post.objects.filter(published_data__lte = timezone.now()).order_by('published_data')
    #이후 posts Query set을 템플릿 컨텍스트에 전달한다.
    #request에는 사용자가 요청하는 모든 것이 들어가있다.
    # {}는 템플릿에 사용하기 위해 매개변수를 추가한다. 형식은 json
    return render(request, 'blog/post_list.html',{'posts':posts})
# Create your views here.
