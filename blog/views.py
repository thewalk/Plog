from django.shortcuts import render
from blog.models import Article
# Create your views here.

def detail(request, article_id):
	detail = Article.objects.get(pk=1)
	context = {'detail': detail}
	return render(request, 'blog/detail.html', context)
