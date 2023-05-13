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
    num=int(request.GET.get('num'))
    score=request.GET.get('score')
   
    length = returnnumquestions(category, level, num)

    if(num>=length):
        return render(request,'result.html',{'score':score,'category':category,'level':level})
    else:
        ques = returnquestion(category,level,num)
        answers,correct_answer=returnanswer(ques)
        return render(request,'question.html',{'level':level,'num':num,'category':category,'ques':ques,'answers':answers,'correct_answer':correct_answer,'score':score})
def result(request):
    level = request.GET.get('level')
    category=request.GET.get('category')

    score=request.GET.get('score')
    return render(request,'result.html',{'score':score,'category':category,'level':level})
        
    
def returnquestionset(category,level,num):
    cat=Category.objects.filter(title=category)[0]
    lev=level.split()[-1]
    lvl=Level.objects.filter(category=cat,level=lev)[0]
    question=Question.objects.filter(level=lvl)
    return(question)

def returnquestion(category, level, num):
    question = returnquestionset(category, level, num)
    return question[num]

def returnnumquestions(category, level, num):
    question = returnquestionset(category, level, num)
    return len(question)

def returnanswer(qn):
    ans=Answer.objects.filter(question=qn)
    correct_answer=Answer.objects.filter(question=qn,is_correct="True")[0].id
    return(ans,correct_answer)

