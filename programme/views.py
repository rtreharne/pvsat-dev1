from django.shortcuts import render
from programme.models import Speaker, Theme
from exhibitors.models import Exhibitor
from sponsors.models import Sponsor
from authors.models import UserProfile, Abstract
from django.contrib.auth.models import User

def programme(request):
    speakers = Speaker.objects.order_by('?')[:]
    themes = Theme.objects.all()
    exhibitors = Exhibitor.objects.all()
    sponsors = Sponsor.objects.all()
    authors = UserProfile.objects.order_by('user__last_name')
    programme_dict = {'speakers': speakers,
                      'themes': themes,
                      'exhibitors': exhibitors,
                      'sponsors': sponsors,
                      'authors': authors}
    return render(request, 'programme.html', programme_dict)

def abstracts(request):
    abstracts = Abstract.objects.all()
    return render(request, 'abstracts.html', {'abstracts': abstracts})
def abstract(request, abstract_id=1):
     abstract = Abstract.objects.get(id=abstract_id)
     dictionary = {'abstract': abstract}
     return render(request, 'abstract.html', dictionary)

def profile(request, user_id=1):
	profile = UserProfile.objects.get(user = User.objects.get(id=user_id))
        abstracts = Abstract.objects.filter(author=profile, status='Accepted')
	dictionary = {'profile': profile,
                      'abstracts': abstracts}
	return render(request, 'profile.html', dictionary)

def theme(request, theme_id=1):
	theme = Theme.objects.get(id=theme_id)
	abstracts = Abstract.objects.filter(theme=theme_id, status='Accepted')
        return render(request, 'theme.html', {'theme': theme, 'abstracts': abstracts})


