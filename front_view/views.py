from django.shortcuts import render

# Create your views here.


def aa():
    a = abs(-3)

import  time
def index(request):
    print('salam')
    for i in range(1000):
        aa()
    return render(request, 'front_view/index.html')