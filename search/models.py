from django.db import models

# Create your models here.

# Store document content
class Document(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()

# Store term frequency in a document
# The score is calculated at the end
# to rank the tfidf
class TermFrequency(models.Model):
    term = models.CharField(max_length=200, null=True, blank=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    frequency = models.IntegerField(default=1)
    score = models.FloatField(default=0)

    
# Store how many document contains a given
# term
class DocFrequency(models.Model):
    term = models.CharField(max_length=200, null=True, blank=True)
    num_docs = models.IntegerField(default=1)