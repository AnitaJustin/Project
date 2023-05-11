from django.shortcuts import render
from .models import Category,Levels,Questions,Answers


def homepage(request):
    return render(request,'home.html')

def nextpage(request):
    categories=Category.objects.all()
    return render(request,'nextpage.html',{'categories':categories})

def levels(request):
    category = request.GET.get('category')
    return render(request,'levels.html',{'category':category})

def info_page(request):
    category = request.GET.get('category')
    level = request.GET.get('level')
    # data=Levels.objects.all()
    return render(request,'info_page.html',{'level':level,'category':category})

def questions(request):
    category=request.GET.get('category')
    level=request.GET.get('level').split()[-1]
    num=request.GET.get('num')
    print(category, level, num)
    question=returnquestion(category,level,num)
    answer=returnanswer(question)
    
    return render(request,'questions.html',{'level':level,'category':category,'question':question,'answer':answer})

def returnquestion(category,level,num):
    c=Category.objects.filter(title=category)[0]
    d=Levels.objects.filter(category=c,level=level)[0]
    qn=Questions.objects.filter(level=d)[int(num)]
    return(qn)
def returnanswer(question):
    answer=Answers.objects.filter(question=question)
    return(answer)
