from django.db import models
from django.contrib import admin

# Create your models here.
class Corpus(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=150)
	source = models.CharField(max_length=150)
	link = models.CharField(max_length=150)
	description = models.TextField()
	time = models.CharField(max_length=15)
	tag = models.CharField(max_length=150)
	organization = models.CharField(max_length=150)
	language = models.CharField(max_length=50)
	target = models.TextField()

class CorpusAdmin(admin.ModelAdmin):
    list_display = ('id','title','tag','time')

admin.site.register(Corpus,CorpusAdmin)



