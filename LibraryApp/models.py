from django.db import models

# Create your models here.
class WordCollection(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    class Meta:
        db_table = 'LibraryApp_wordcollection'

    def __str__(self):
        return self.title
    
class Word(models.Model):
    collection = models.ForeignKey(WordCollection, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.word