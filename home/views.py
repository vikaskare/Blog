from django.shortcuts import render


# Create your views here.
def index(request, *args, **kwargas):
    return render(request=request, template_name="index.html")
