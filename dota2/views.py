from django.shortcuts import render

# Simple page name 'home'
def home(request):
    template = "home.html"
    context = {}
    return render(request, template, context)

