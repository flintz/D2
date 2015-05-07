from django.shortcuts import render

# Create your views here.
# Simple page name 'home'
def home(request):
    template = "home.html"
    context = {}
    return render(request, template, context)
