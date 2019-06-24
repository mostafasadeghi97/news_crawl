from django.http import HttpResponse
from django.shortcuts import render
from search.suggest import rank, suggessted_terms
import json

def search_term(request):
    query = request.GET.get('query')
    context = None
    if query:
        print(query)
        print(rank(query))
        context = {'docs': rank(query), 'query': query}
    return render(request, 'search/home.html', context)

def term_autocomplete(request):
    term = request.GET.get('query')
    suggested_terms = search_term(term)
    result = {}
    result['suggestions'] = suggested_terms
    return HttpResponse(json.dumps(result))