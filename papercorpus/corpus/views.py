from django.shortcuts import render
from corpus.models import Corpus
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    corpus = Corpus.objects.all()
    return render_to_response('index.html',{'corpus':corpus})

def detail(request):
	id = request.GET["id"]
	corpus = Corpus.objects.get(id=id)
	return render_to_response('detail.html',{'corpus':corpus})
