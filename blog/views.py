from django.shortcuts import render
from blog.models import Article,Category,Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')
def article_detail(request, article_id, category_type, category_name, tag_name):
    detail = Article.objects.get(pk=article_id)
    if category_name:
        article_list = Article.objects.filter(category__category_name = category_name).order_by('publish_time')
    elif tag_name:
        tag = Tag.objects.get(tag_name__exact = tag_name)
        article_list = tag.article_set.all().filter(category__category_type__categoryType_name__exact = category_type).order_by('publish_time')
    else:
        article_list = Article.objects.filter(category__category_type__categoryType_name__exact = category_type).order_by('publish_time')
    for current in article_list:
        if current.publish_time > detail.publish_time:
            break
    next = current
    if next == detail:
        next = ''

    if category_name:
        article_list = Article.objects.filter(category__category_name = category_name).order_by('-publish_time')
    elif tag_name:
        tag = Tag.objects.get(tag_name__exact = tag_name)
        article_list = tag.article_set.all().filter(category__category_type__categoryType_name__exact = category_type).order_by('-publish_time')
    else:
        article_list = Article.objects.filter(category__category_type__categoryType_name__exact = category_type).order_by('-publish_time')
    for current in article_list:
        if current.publish_time < detail.publish_time:
            break
    previous = current
    if previous == detail:
        previous = ''

    category_list = Category.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')
    tag_list = Tag.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')
    context = { 
                'category_name':category_name,
                'tag_name':tag_name,
                'category_type':category_type,
                'detail': detail,
                'next':next,
                'previous':previous,
                'category_list':category_list,
                'tag_list':tag_list
    }
    return render(request, 'blog/article/article_detail.html', context)

def article_list_by_category_type(request, category_type):
    article_list = Article.objects.filter(category__category_type__categoryType_name__exact = category_type).order_by('-publish_time')
    category_list = Category.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')
    tag_list = Tag.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')

    paginator = Paginator(article_list,12)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num.pages)
    context = {
                'category_type':category_type,
                'articles':articles,
                'category_list':category_list,
                'tag_list':tag_list}
    return render(request, 'blog/article/article_list.html', context)

def article_list_by_category_name(request, category_name, category_type):
    article_list = Article.objects.filter(category__category_name = category_name).order_by('-publish_time')
    category_list = Category.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')
    tag_list = Tag.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')

    paginator = Paginator(article_list,12)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num.pages)
    context = {
                'category_type':category_type,
                'category_name':category_name,
                'articles':articles,
                'category_list':category_list,
                'tag_list':tag_list}
    return render(request, 'blog/article/article_list.html', context)

def article_list_by_tag_name(request, tag_name, category_type):
    tag = Tag.objects.get(tag_name__exact = tag_name)
    article_list = tag.article_set.all().filter(category__category_type__categoryType_name__exact = category_type).order_by('-publish_time')
    category_list = Category.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')
    tag_list = Tag.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')

    paginator = Paginator(article_list,12)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num.pages)
    context = {
                'category_type':category_type,
                'tag_name':tag_name,
                'articles':articles,
                'category_list':category_list,
                'tag_list':tag_list}
    return render(request, 'blog/article/article_list.html', context)
