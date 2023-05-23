from django.shortcuts import render
from .models import *
from random import shuffle


# Create your views here.
def homepage(request):
    return render(request,'home.html')

def nextpage(request):
    category=Category.objects.all()
    return render(request,'nextpage.html',{'category': category})

def levels(request):
    category=request.GET.get('category')
    category_obj = Category.objects.get(title=category)
    levels = Level.objects.filter(category=category_obj)
    levels=list(levels)
    unlock = user_progress.objects.filter(is_completed=True)
    unlock=[i.level.id for i in unlock]
    # unlock=list(unlock)

    return render(request,'levels.html',{'category':category,'unlock':unlock,'levels':levels})


def info_page(request):
    level = request.GET.get('level')
    lev=level.split("-")[-1]
    category=request.GET.get('category')
    return render(request,'info_page.html',{'level':level,'category':category,'lev':lev})

def question(request):
    level = request.GET.get('level')
    category=request.GET.get('category')
    num=int(request.GET.get('num'))
    score=int(request.GET.get('score'))
    min_correct=int(request.GET.get('min_correct'))
    duration=request.GET.get('duration')
    length = returnnumquestions(category, level, num)
    lvl,nxtlvl=returnlev(category,level)
    if(num>=length):
         if(score >= min_correct):
             obj=user_progress.objects.filter(level=nxtlvl)[0]
             obj.is_completed=True
             obj.save()
         return render(request,'result.html',{'score':score,'category':category,'level':level,'min_correct':min_correct,'lvl':lvl})
    else:
        # if(num == 0):
        #     quesset = returnquestionset(category,level,num)
        #     shuffle(quesset)
        # if num == 0:
        #     if 'quesset' not in request.session:
        #         quesset = returnquestionset(category, level, num)
        #         shuffle(quesset)
        #         request.session['quesset'] = quesset
        #         request.session.save()
        # else:
        #     quesset = request.session['quesset']
        quesset = returnquestionset(category,level,num)
        ques=quesset[num]
        answers,correct_answer=returnanswer(ques)
        return render(request,'question.html',{'level':level,'num':num,'category':category,'ques':ques,'answers':answers,'correct_answer':correct_answer,'score':score,'min_correct':min_correct,'duration':duration})
def result(request):
    level = request.GET.get('level')
    category=request.GET.get('category')
    min_correct=int(request.GET.get('min_correct'))
    score=int(request.GET.get('score'))
    lvl,nxtlvl=returnlev(category,level)
    if(score>=min_correct):
             obj=user_progress.objects.filter(level=nxtlvl)[0]
             obj.is_completed=True
             obj.save()
    return render(request,'result.html',{'score':score,'category':category,'level':level,'min_correct':min_correct,'lvl':lvl})
        
    
def returnquestionset(category,level,num):
    cat=Category.objects.filter(title=category)[0]
    lev=level.split("-")[-1]
    lvl=Level.objects.filter(category=cat,level=lev)[0]
    question=Question.objects.filter(level=lvl)
    question=list(question)
    return(question)

def returnquestion(category, level, num):
    question = returnquestionset(category, level, num)
    # if(num == 0):
    #     shuffle(question)
    # return question[int(num)]
    return question[num]

def returnnumquestions(category, level, num):
    question = returnquestionset(category, level, num)
    return len(question)

def returnanswer(qn):
    ans=Answer.objects.filter(question=qn)
    ans=list(ans)
    shuffle(ans)
    correct_answer=Answer.objects.filter(question=qn,is_correct="True")[0].id
    return(ans,correct_answer)

def returnlev(category,level):
    cat=Category.objects.filter(title=category)[0]
    lev=level.split("-")[-1]
    nexlev=int(lev)+1
    lvl=Level.objects.filter(category=cat,level=lev)[0]
    nextlvl=Level.objects.filter(category=cat,level=nexlev)[0]
    return(lvl,nextlvl)