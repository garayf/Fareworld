from django.shortcuts import render

# Create your views here.
def card_page_resume(request):
    return render(request, 'card/resume.html')

def card_page_landing(request):
    return render(request, 'card/landing.html')