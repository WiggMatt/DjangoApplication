from django.shortcuts import render, redirect


# Create your views here.

def main(request):
    return render(request, 'DjangoApplication/main.html', {"title": "Main page"})

def about(request):
    return render(request, 'DjangoApplication/about.html', {"title": "About page"})

def more(request):
   return render(request, 'DjangoApplication/more.html', {"title": "More page"})

def navbar(request):
    return redirect("https://getbootstrap.com/docs/5.3/components/navbar/#how-it-works")
