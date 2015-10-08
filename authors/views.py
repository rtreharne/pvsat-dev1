from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from authors.forms import UserForm, UserProfileForm, AbstractForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from authors.models import UserProfile, Abstract
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

@login_required
def submit_paper(request, abstract_id=1):
	user = request.user
	inst = Abstract.objects.get(id=abstract_id)
        
	if inst.author.user.id != user.id:
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            submitted = False
            if request.method =='POST':
                abstract_form = AbstractForm(data=request.POST, instance=inst)
                if abstract_form.is_valid():
                    abstract = abstract_form.save(commit=False)

                    if 'upload' in request.FILES:
                        abstract.upload = request.FILES['upload']
                        
                    abstract.save()

                    submitted = True

                else:
                    print abstract_form.errors

            else:
                abstract_form = AbstractForm(instance=inst)

            return render(request, 'submit_paper.html', {'abstract_form': abstract_form})

@login_required
def update_profile(request):
    submitted = False
    inst = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST, instance=inst)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user= request.user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            submitted=True

        else:
            print profile_form.errors
        
    else:
        profile_form = UserProfileForm(instance=inst)
    
    return render(request, 'update_profile.html', {'profile_form': profile_form, 'submitted': submitted})

@login_required
def submit_abstract(request):
    submitted = False

    if request.method == 'POST':
        abstract_form = AbstractForm(request.POST, request.FILES)
		
        if abstract_form.is_valid():
            abstract = abstract_form.save(commit=False)
            abstract.author = UserProfile.objects.get(user=request.user)

            if abstract.tags == "":
                abstract.tags = None
            else:
                abstract.tags = abstract.tags.replace(", ", ",")
                abstract.tags = abstract.tags.replace(",  ", ",")
                
                

            try:
                obj = Abstract.objects.latest('id')
                id = obj.id + 1
            except ObjectDoesNotExist:
                id = 0

            abstract.unique_id = 'PVSAT12_%s' % (str(id).zfill(3))

            if 'upload' in request.FILES:
			   abstract.upload = request.FILES['upload']

            #Email confirmation to user
            subject = 'Abstract Submission Confirmation: %s' % (abstract.unique_id)

            text_content = render_to_string("abs_sub_conf.txt", {'abstract': abstract, 'URL': settings.SITE_URL})
            html_content = render_to_string("abs_sub_conf.html", {'abstract': abstract, 'URL': settings.SITE_URL})

            email = abstract.author.user.email

            msg1 = EmailMultiAlternatives(subject, text_content, '', [email])
            msg1.attach_alternative(html_content, "text/html")

            #Email confirmation to admin

            subject = 'Abstract %s submitted by %s %s' % (abstract.unique_id, abstract.author.user.first_name, abstract.author.user.last_name)

            text_content = render_to_string("abs_to_admin.txt", {'abstract': abstract, 'URL': settings.SITE_URL})

            msg2 = EmailMultiAlternatives(subject, text_content, '', [settings.ADMIN_EMAIL])

            if settings.EMAIL_STATUS:
                msg1.send()
                msg2.send()
                

            abstract_form.save()

            submitted = True



        else:
			print abstract_form.errors
    
    else:	    
	    abstract_form = AbstractForm()
	
    return render(request, 'submit_abstract.html', {'abstract_form': abstract_form, 'submitted': submitted})

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    invalid = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Your account is disabled")

        else:
            invalid = True 
            return render(request, 'login.html', {'invalid': invalid})
                
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'login.html', {'invalid': invalid})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def dashboard(request):
    user = request.user
    profile = UserProfile.objects.get(user_id=user.id)
    abstracts = Abstract.objects.filter(author=profile)
    return render(request, 'dashboard.html', {'user':user, 'profile': profile, 'abstracts': abstracts})
    
