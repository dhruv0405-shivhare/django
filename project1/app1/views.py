

# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
def home (request):
    # name='Dhruv'
    # return HttpResponse('<h1 style="background-color: yellow;">hello</h1>')
    # return render (request,"index.html",{'name':name})
    # return redirect("https://chatgpt.com/")
    data = {'name':'dhruv',
            'age':'22',
            'active':True,
            'other':None
            }
    return JsonResponse(data)