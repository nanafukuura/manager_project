from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import AppForm
# Create your views here.
def index(request):
    params={
    'title':'hello',
    'msg':'your data',
    'form': AppForm()
        }
    if (request.method=='POST'):
        params['msg']='名前:'+request.POST['name']+\
            '<br>メール:'+request.POST['mail']+\
            '<br>年齢:'+request.POST['age']
        params['form']=AppForm(request.POST)
    return render(request,'app/index.html',params)
