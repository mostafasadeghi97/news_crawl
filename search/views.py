from django.http import HttpResponse, JsonResponse
from django.shortcuts import render , get_object_or_404
from search.suggest import rank, suggessted_terms
import json
from .models import Document, DocFrequency, TermFrequency


def get_by_category(reqHttpResponseuest, category_id):
    news = Document.objects.filter(category=category_id).values('summary','title')
    return JsonResponse({'news':news})


def get_detail_news(request, news_id):
    news = get_object_or_404(Document, id=news_id)
    return JsonResponse({'news':news})





def search_term(request):
    query = request.GET.get('query')
    context = None
    if query:
        print(query)
        print(rank(query))
        context = {'docs': rank(query), 'query': query}
    return render(request, 'search/home.html', context)

def term_autocomplete(request):
    print(request.GET)
    term = request.GET.get('query')
    suggested_terms = suggessted_terms(term)
    result = {}
    result['suggestions'] = suggested_terms
    return JsonResponse(result)