

from django.db.models import Sum
from .models import Document, DocFrequency, TermFrequency
import math
import hazm

def rank(query):
    
    terms = hazm.word_tokenize(query)
        
    rows = TermFrequency.objects.filter(term__in=terms)\
                                .values('id','document')\
                                .annotate(total_score=Sum('score'))\
                                .order_by('-total_score')[:100]

    print([x['id'] for x in rows])
        
    doc_ids = [x['document'] for x in rows]
    docs = []
    for i in range(len(doc_ids)):

        doc = Document.objects.get(id=doc_ids[i])
        doc.score = math.ceil(rows[i]['total_score']*100)/100
        docs.append(doc)
    return docs
    

def suggessted_terms(term):
    doc_freqs = DocFrequency.objects.filter(term__startswith=term).order_by('-num_docs')[:10]
    suggested_terms = [x.term for x in doc_freqs]
    return suggested_terms

