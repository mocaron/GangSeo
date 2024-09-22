from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    #return HttpResponse("강서공고 안녕")
    #return render(request, 'main.html')
    lists = Memo.obejcts.all()
    data = {'lists': lists}
    return render(request 'main.html', data)
    


def create(request):
    content = request.POST['memoContent']
    #return HttpResponse("메모작성 내용 = "+content)
    usermemo = Memo(text = content)
    usermemo.save()
    return HttpResponseRedirect(reverse('index'))

