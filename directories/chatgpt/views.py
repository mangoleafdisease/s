from django.shortcuts import render, redirect
from .models import Curso, User, Chat , Rating
from django.contrib import messages
from . forms import ProductForm
from django.db.models import Count
# Create your views here.
from django.http import JsonResponse
from random import randrange
import openai
import datetime
datetime.datetime.now().strftime ("%Y%m%d")
from random import randrange 
num = randrange(100000, 1000000)
from django.contrib.auth import logout
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date, timedelta
from .models import QuestionAnswer
import openai
import json

# Create your views here.
open_api_key = "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"
openai.api_key = open_api_key

SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 5 # 5 seconds for testing
SESSION_SAVE_EVERY_REQUEST = True

session1 = str(randrange(100000, 1000000))+datetime.datetime.now().strftime ("%Y%m%d")

def indexhom(request):
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    seven_days_ago = date.today() - timedelta(days=7)
    
    questions = QuestionAnswer.objects.filter(user=request.user)
    t_questions = questions.filter(created=today)
    y_questions = questions.filter(created=yesterday)
    s_questions = questions.filter(created__gte=seven_days_ago, created__lte=today)
    
    context = {"t_questions":t_questions, "y_questions": y_questions, "s_questions": s_questions}

    return render(request, "chatbot.html", context)



def ask_openai(message):
    response = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:personal::8etNOvnh",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
            
    ],

    
)
    
    answer = response['choices'][0]['message']['content']
    return answer


def getValue(request):
    data = json.loads(request.body)
    message = data["msg"] 
    response = ask_openai(message)
    code = str(randrange(100000, 1000000))+datetime.datetime.now().strftime ("%Y%m%d")
    QuestionAnswer.objects.filter(year_level=request.session['person']['year_level'],course=request.session['person']['course'],session=session1)
    QuestionAnswer.objects.create(user = "normi", question=message, answer=response,year_level=request.session['person']['year_level'],course=request.session['person']['course'], code=code, session=session1)

    return JsonResponse({"msg": message, "res": response})
    
    

def home(request):
    request.session.clear()
    request.session.flush()
    if 'year_level' in request.session:
        num = "1"
    else:
        num = "0"
     
    cursosListados = QuestionAnswer.objects.all()

    if request.method == 'POST':
        request.session['person'] = {'course':request.POST['course'],'year_level':request.POST['year_level']}
        if request.POST['feed1']=="0":
            
            num = "1"
            cursosListados = QuestionAnswer.objects.filter(year_level=request.session['person']['year_level'],course=request.session['person']['course'],session=session1)
            return render(request, 'chats.html',{"chats": cursosListados,"num": num})
        else:
            cursosListados = QuestionAnswer.objects.filter(year_level=request.session['person']['year_level'],course=request.session['person']['course'],session=session1)
            return render(request, 'chats.html',{"chats": cursosListados})
    else:
        return render(request, "chats.html", {"chats": cursosListados,"num": num})
    


def register_user(request):
    return render(request, 'register.html')

def chart(request):
    course = QuestionAnswer.objects.values('course').annotate(count=Count('course'))
    year = QuestionAnswer.objects.values('year_level').annotate(count1=Count('year_level'))
    answer = QuestionAnswer.objects.values('answer').annotate(count2=Count('answer'))
    form = ProductForm()
    cursosListados = QuestionAnswer.objects.all()
    total = QuestionAnswer.objects.count()

    context = {
        "course": course,
        "year_level": year,
        "form": form,
        "total": total,
        "answer":answer,
        "chats": cursosListados
    
    }

    if not request.user.is_authenticated:
        # User has visited the website before

        request.session['username'] = True
        return redirect('home')
    else:
        
        # User is visiting the website for the first time
        return render(request, 'sample.html', context)

    
def main(request):
    return render(request, 'chatbox.html')  
  
def qanda(request):
    if request.user.is_authenticated==False:
        return redirect('home')
    
    cursosListados = QuestionAnswer.objects.values('question').annotate(count=Count('question'))
    page_title = 'dashboard'
    return render(request, 'question.html',{"chats": cursosListados})


def editView(request, question):
    curso = QuestionAnswer.objects.filter(question=question)
    return render(request, "questionView.html", {"curso": curso})



def courseView(request, code):
    curso = QuestionAnswer.objects.filter(course=code)
    return render(request, "courseView.html", {"courseView": curso})


def course(request):
    cursosListados = QuestionAnswer.objects.values('course').distinct()
    return render(request, 'course.html',{"course": cursosListados})




def levelView(request, code):
    curso = QuestionAnswer.objects.filter(year_level=code)
    return render(request, "levelView.html", {"levelView": curso})


def level(request):
    cursosListados = QuestionAnswer.objects.values('year_level').distinct()
    return render(request, 'level.html',{"year_level": cursosListados})

def feedback(request):
    cursosListados = QuestionAnswer.objects.exclude(feedback='')
    return render(request, 'feedback.html',{"feedback": cursosListados})


def change(request):
    page_title = 'changepass'
    return render(request, 'changepass.html',{'cat_landing': "cat_landing",'page_title':page_title})


    

def login_user(request):
    err = None
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
        else:
            err = "Invalid Credentials"
        
        
    context = {"error": err}
    return render(request, "login.html", context)
    

def register(request):
    code="345435"
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirmpassword']

    user = User.objects.create(code=code, username=username, password=password, email=email, firtname=firstname, lastname=lastname)
    return render(request, "register.html", {"user": user})

def session(request):
    if request.method == 'POST':
        code = request.POST['code']
        feedback = request.POST['editor1']
        curso = QuestionAnswer.objects.get(code=code)
        curso.feedback = feedback
        curso.save() 
        return render(request, 'chats.html')
    else:
        return render(request, 'chats.html')



def dashboard(request):
    course = QuestionAnswer.objects.values('course').annotate(count=Count('course'))
    year = QuestionAnswer.objects.values('year_level').annotate(count1=Count('year_level'))
    answer = QuestionAnswer.objects.values('answer').annotate(count2=Count('answer'))
    form = ProductForm()
    cursosListados = QuestionAnswer.objects.all()
    total = QuestionAnswer.objects.count()

    context = {
        "course": course,
        "year_level": year,
        "form": form,
        "total": total,
        "answer":answer,
        "chats": cursosListados
    
    }

    if not request.user.is_authenticated:
        # User has visited the website before

        request.session['username'] = True
        return redirect('home')
    else:
        
        # User is visiting the website for the first time
        return render(request, 'chart.html', context)


def signout(request):
    logout(request)
    return render(request, 'chats.html')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars']

def rate(request, year_level):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.year_level = year_level
            # I-save ang rating sa database
            rating.save()
            return redirect('home')  # I-redirect sa kung saan mo nais
    else:
        form = RatingForm()

    context = {'form': form, 'year_level': year_level}
    return render(request, 'rate.html', context)

def get_ratings_count(request):
    ratings_count = {
        'first_year': Rating.objects.filter(year_level=1).count(),
        'second_year': Rating.objects.filter(year_level=2).count(),
        'third_year': Rating.objects.filter(year_level=3).count(),
        'fourth_year': Rating.objects.filter(year_level=4).count(),
        # ... Atbp para sa iba pang year levels
    }
    return JsonResponse(ratings_count)








