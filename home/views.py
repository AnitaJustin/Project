from django.shortcuts import render
from .models import *


# Create your views here.
def homepage(request):
    return render(request,'home.html')

def nextpage(request):
    category=Category.objects.all()
    return render(request,'nextpage.html',{'category': category})

def levels(request):
    category=request.GET.get('category')
    return render(request,'levels.html',{'category':category})

def info_page(request):
    level = request.GET.get('level')
    category=request.GET.get('category')
    return render(request,'info_page.html',{'level':level,'category':category})

def question(request):
    level = request.GET.get('level')
    category=request.GET.get('category')
    num=request.GET.get('num')
    ques=returnquestion(category,level,num)
    answers=returnanswer(ques)

    return render(request,'question.html',{'level':level,'num':num,'category':category,'ques':ques,'answers':answers})

def returnquestion(category,level,num):
    cat=Category.objects.filter(title=category)[0]
    lev=level.split()[-1]
    lvl=Level.objects.filter(category=cat,level=lev)[0]
    question=Question.objects.filter(level=lvl)
    qn=question[0]
    return(qn)
def returnanswer(qn):
    ans=Answer.objects.filter(question=qn)
    return(ans)


