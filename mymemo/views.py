from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    #return HttpResponse("강서공고 안녕")
    return render(request, 'main.html')



def create(request):
    content = request.POST['memoContent']
    return HttpResponse("메모작성 내용 = "+content)
