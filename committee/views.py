from django.shortcuts import render
from committee.models import Member

def committee(request):
    members = Member.objects.all()
    return render(request, 'committee.html', {'members': members})


