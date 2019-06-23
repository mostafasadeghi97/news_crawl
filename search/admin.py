from django.contrib import admin


from .models import DocFrequency, Document, TermFrequency
# Register your models here.


admin.site.register(DocFrequency)
admin.site.register(Document)
admin.site.register(TermFrequency)
