from django.shortcuts import render
from blog.models import Article
from django.core.exceptions import ObjectDoesNotExist

def articles(request):
    try:
        articles = Article.objects.order_by('-pub_date')
    except ObjectDoesNotExist:
        articles = None
   

    return render(request, 'articles.html', {'articles': articles})

def article(request, article_id=1):
	article= Article.objects.get(id=article_id)
	return render(request, 'article.html', {'article': article})
	


