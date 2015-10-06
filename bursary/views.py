from django.shortcuts import render
from bursary.forms import BursaryForm 

def application(request):
    submitted = False

    if request.method == 'POST':
        bursary_form = BursaryForm(data=request.POST)
		
        if bursary_form.is_valid():
			applicant = bursary_form.save()

			submitted = True

        else:
			print bursary_form.errors
    
    else:	    
	    bursary_form= BursaryForm()
	
    return render(request, 'bursary.html', {'bursary_form': bursary_form, 'submitted': submitted})

