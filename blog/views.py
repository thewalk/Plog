from django.shortcuts import render
from blog.models import Article,Category,Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def qrcode(request):
    return render(request, 'blog/others/qrcode.html')

def artilce_base(request):
    category_type = request.GET.get('category_type')
    dict1 = query_category_tag_list_by_category_type(category_type)
    dict2 = {'category_type':category_type}
    context = dict(dict1.items()+dict2.items())
    return render(request,'blog/article/article_base.html', context)

def article_detail(request):
    article_id = request.GET.get('article_id')
    category_id = request.GET.get('category_id')
    tag_id = request.GET.get('tag_id')
    context = query_article_detail(article_id,category_id,tag_id)
    return render(request, 'blog/article/article_detail.html', context)

def query_article_detail(article_id, category_id, tag_id):
    detail = Article.objects.get(pk = article_id)
    if category_id:
        article_list = Article.objects.filter(category_id = category_id).order_by('publish_time')
    elif tag_id:
        tag = Tag.objects.get(pk = tag_id)
        article_list = tag.article_set.all().order_by('publish_time')
    else:
        article_list = Article.objects.order_by('publish_time')
    for current in article_list:
        if current.publish_time > detail.publish_time:
            break
    next = current
    if next == detail:
        next = ''

    if category_id:
        article_list = Article.objects.filter(category_id = category_id).order_by('-publish_time')
    elif tag_id:
        tag = Tag.objects.get(pk = tag_id)
        article_list = tag.article_set.all().order_by('-publish_time')
    else:
        article_list = Article.objects.order_by('-publish_time')
    for current in article_list:
        if current.publish_time < detail.publish_time:
            break
    previous = current
    if previous == detail:
        previous = ''

    context = {
                'detail': detail,
                'next':next,
                'previous':previous,
    }
    return context

def article_list(request):
    category_type = request.GET.get('category_type')
    category_id = request.GET.get('category_id')
    tag_id = request.GET.get('tag_id')
    page = request.GET.get('page')
    context = query_article_list(category_type,category_id,tag_id,page)
    return render(request,"blog/article/article_list.html",context)


def query_article_list(category_type,category_id,tag_id,page):
    if bool(category_id):
        context = query_article_list_by_category_id(category_id, page)
    elif bool(tag_id):
        context =query_article_list_by_tag_id(tag_id, page)
    else:
        context = query_article_list_by_category_type(category_type, page)

    return context

def query_category_tag_list_by_category_type(category_type):
    category_list = Category.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')
    tag_list = Tag.objects.filter(category_type__categoryType_name__exact = category_type).order_by('create_time')
    context = {'tag_list':tag_list,
                'category_list':category_list,
    }
    return context

def query_article_list_by_category_type(category_type, page):
    article_list = Article.objects.filter(category__category_type__categoryType_name__exact = category_type).order_by('-publish_time')
    paginator = Paginator(article_list,6)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num.pages)
    context = {'articles':articles}
    return context

def query_article_list_by_category_id(category_id, page):
    category = Category.objects.get(pk = category_id)
    article_list = Article.objects.filter(category_id = category_id).order_by('-publish_time')
    paginator = Paginator(article_list,6)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num.pages)
    context = {'articles':articles,
    }
    return context

def query_article_list_by_tag_id(tag_id, page):
    tag = Tag.objects.get(pk = tag_id)
    tag = Tag.objects.get(id__exact = tag_id)
    article_list = tag.article_set.all().order_by('-publish_time')
    paginator = Paginator(article_list,6)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num.pages)
    context = {'articles':articles,
    }
    return context
