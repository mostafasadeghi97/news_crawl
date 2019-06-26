from django.shortcuts import render
from search.models import Document
from django.http import JsonResponse
# Create your views here.

def index(request):
    query = Document.objects.all().values('title','date','category','image_link')[:6]
    pop_query = Document.objects.all().values('title','date','category','image_link','summary')[:90:10]
    
    return render(request, 'front_view/index.html',{'news':query,'popular_news':pop_query})


def category(request, category_id):
    news = Document.objects.filter(category=category_id).values('title','date','summary')
    return JsonResponse({'news':news})