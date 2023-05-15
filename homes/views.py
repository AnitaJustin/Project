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
    level=request.GET.get('level')
    num=request.GET.get('num')
    scr=request.GET.get('score')
    min_correct=request.GET.get('min_correct')
    length=returnquestionlength(category,level)
    if(length>=int(num)+1):
        question=returnquestion(category,level,num)
        answer, correctAnswer=returnanswer(question)
        return render(request,'questions.html',{'level':level, 'num':num, 'category':category,'question':question,'answer':answer, 'correctAnswer': correctAnswer, 'score':scr, 'min_correct':min_correct})
    else:
        return render(request,'result.html',{'level':level, 'num':num, 'category':category, 'score':scr,'min_correct':min_correct})

def returnquestion(category,level,num):

    c=Category.objects.filter(title=category)[0]
    d=Levels.objects.filter(category=c,level=level.split()[-1])[0]
    qn=Questions.objects.filter(level=d)[int(num)]
    return(qn)

def returnquestionlength(category,level):
    c=Category.objects.filter(title=category)[0]
    d=Levels.objects.filter(category=c,level=level.split()[-1])[0]
    qn=Questions.objects.filter(level=d)
    return(len(qn))

def returnanswer(question):
    answer=Answers.objects.filter(question=question)
    correctAnswer = Answers.objects.filter(question=question, is_correct=True)[0].id
    return(answer, correctAnswer)

def result(request):
    category=request.GET.get('category')
    level=request.GET.get('level')
    scr=request.GET.get('score')
    min_correct=request.GET.get('min_correct')
    return render(request,'result.html',{'category':category, 'level':level, 'score':scr,'min_correct':min_correct})