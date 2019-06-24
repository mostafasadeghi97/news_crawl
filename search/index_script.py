



from .models import DocFrequency, Document, TermFrequency
from django.db.models import Count
import hazm
import math

from bulk_update.helper import bulk_update



def get_freq_data(data):
    tokens = hazm.word_tokenize(data)
    freq_dict = {}

    for token in tokens:
        if token not in freq_dict:
            freq_dict[token] =1
        else:
            freq_dict[token] +=1

    lemmatize_dict = {}
    lemmatizer = hazm.Lemmatizer()
    for term in freq_dict.keys():
        lemmatize_term = lemmatizer.lemmatize(term)
        value = freq_dict[term]

        if lemmatize_term in lemmatize_dict:
            lemmatize_dict[lemmatize_term] +=value
        else:
            lemmatize_dict[lemmatize_term] = value

    return lemmatize_dict

def index_term_freqs():
    documents = Document.objects.all()
    for doc in documents:
        title = doc.title
        if title is None:
            title == ""
        summary = doc.summary
        if summary == None:
            summary = ""
         
        content = doc.content
        if content == None:
            content = ""
        
        data = str(title) + " " + summary + " " + content
        freq_dict = get_freq_data(data)

        terms_frequencys = []

        for term in freq_dict:
            term_freq = TermFrequency()
            term_freq.term = term
            term_freq.frequency = freq_dict[term]
            term_freq.document = doc
            term_freq.score = 0
            terms_frequencys.append(term_freq)

        TermFrequency.objects.bulk_create(terms_frequencys)

    

def index_docs_freq():

    if DocFrequency.objects.all().exists():
        return
    

    query = TermFrequency.objects.values('term').annotate(num_docs=Count('term'))

    doc_freqs = [DocFrequency(**obj) for obj in query]

    

    DocFrequency.objects.bulk_create(doc_freqs)

    n = len(doc_freqs)

    term_freq_query = TermFrequency.objects.all()

    for item in term_freq_query:
        doc_freq = DocFrequency.objects.filter(term=item.term)[0]
        item.score = item.frequency * math.log10(n / doc_freq.num_docs)
        

    bulk_update(term_freq_query)

    

if __name__ == '__main__':
    index_term_freqs()
    index_docs_freq()
    print('Done')


