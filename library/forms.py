from mongoengine.django.forms import DocumentForm

class CrateWordsCollectionForm(DocumentForm):
    class Meta:
        model = user
        fields = ['title', 'language']