from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home_page_view(request):
    now = datetime.now()

    return render(request, "FrisbeeApp\home_page.html",
           {
                'title': 'Welcome to my Frisbee App',
                'message': 'message!!!',
                'content': "on " + now.strftime("%A, %d %B, %Y at %X")
           })

