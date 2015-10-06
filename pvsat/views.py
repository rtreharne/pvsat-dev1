from django.shortcuts import render
from sponsors.models import Sponsor
from programme.models import Speaker
from committee.models import Member
from exhibitors.models import Exhibitor
from blog.models import Article
from django.core.exceptions import ObjectDoesNotExist
from random import shuffle

def home(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.order_by('?')[:]
    try:
        article = Article.objects.latest('pub_date')
    except ObjectDoesNotExist:
        article = None

    dict = {'speakers': speaker_list,
            'sponsors': sponsor_list,
            'articles': article}
    return render(request, 'home.html', dict)

'''
def home(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    sponsor_dict = {'sponsors': sponsor_list,
			        'speakers': speaker_list}
    return render(request, 'home.html', sponsor_dict)

def chunk(a):
    b = list(a)
    shuffle(b)
    chunk_list = []
    for i in range (0, len(b), 5):
        chunk = b[i:i+5]
        chunk_list.append(chunk)
    return chunk_list

def bootstrap(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    speaker_chunk = chunk(speaker_list)
    sponsor_dict = {'sponsors': sponsor_list,
	            'speakers': speaker_chunk}
    return render(request, 'bootstrap.html', sponsor_dict)

def bare(request):
    sponsor_list = Sponsor.objects.all()
    speaker_list = Speaker.objects.all()
    committee_list = Member.objects.all()
    exhibitor_list = Exhibitor.objects.all()
    sponsor_dict = {'sponsors': sponsor_list,
	            'speakers': speaker_list,
                    'committee': committee_list,
                    'exhibitors': exhibitor_list,}
    return render(request, 'bare.html', sponsor_dict)
    '''
