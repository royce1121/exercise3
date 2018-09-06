from .models import Student, Section, Enrollment
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NameForm, SearchForm, RegForm, SubAdd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def create(request):
	if request.POST:
		username = request.POST['user']
		password = request.POST['pass']
		email = request.POST['mail']
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		return render(request, 'registration/login.html', {})

#def logout_view(request):
#    logout(request)
#    return render(request, 'exer3/list.html', {})

def software(request):
	first = Student.objects.all()
	return render(request, 'exer3/software.html', {'first':first})

def subject(request, pk):
    post = get_object_or_404(Section, pk=pk)
    if post.name == "Software":
        first = Student.objects.filter(section__name='Software')
        return render(request, 'exer3/software.html', {'first': first})

    elif post.name == "Hardware":
        first = Student.objects.filter(section__name='Hardware')
        return render(request, 'exer3/software.html', {'first': first})

    else:
        first = Student.objects.filter(section__name='Networking')
        return render(request, 'exer3/software.html', {'first': first})

def signup(request):
    return render(request, 'exer3/LoginPage.html', {})


def list(request):
	#first = Student.objects.filter(section__name='First')
	sect = Section.objects.all()
	return render(request, 'registration/login.html', {'sect': sect})
	#return render(request, 'exer3/list.html', {'first': first})

def check(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                first = Student.objects.filter(section__name='Hardware')
                return render(request, 'exer3/profile.html', {'first': first})
        else:
        	return render(request, 'registration/list.html', {})

def student(request):
    stud = Student.objects.all()
    sect = Enrollment.objects.all()
    form = SearchForm()
    return render(request, 'exer3/student.html', {'stud': stud , 'sect': sect})

@login_required
def profile(request):   
    return render(request, 'exer3/profile.html', {})
    
def remove(request, pk):
    post = get_object_or_404(Enrollment, pk=pk)
    post = Student.objects.filter(name=post.student)
    post.delete()
    sect = Enrollment.objects.all()
    form = SearchForm()
    return render(request, 'exer3/student.html', {'sect': sect})

def remove1(request, pk):
    post = get_object_or_404(Student, pk=pk)
    post.delete()
    first = Student.objects.all()
    form = SearchForm()
    return render(request, 'exer3/software.html', {'first': first, 'form': form})

def new(request):
    form = NameForm()
    return render(request, 'exer3/new.html', {'form': form})

def search(request):
    if request.POST:
        search = request.POST['srch']
        sect = Enrollment.objects.filter(student__name__icontains=search)
        if sect.exists():
        	form = SearchForm()
       		return render(request, 'exer3/student.html', {'sect': sect, 'form': form})

        else:
        	sect = Enrollment.objects.filter(section__name__icontains=search)
        	form = SearchForm()
        	return render(request, 'exer3/student.html', {'sect': sect,'form': form})

def search1(request):
    if request.POST:
        search = request.POST['srch']
        first = Student.objects.filter(name__icontains=search)
        form = SearchForm()
        return render(request, 'exer3/software.html', {'first': first}, {'form': form})

def add(request):
    if request.POST:
        form = RegForm()
        return render(request, 'exer3/add.html', {'form': form})

def add1(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            name = form['name'].value()
            subject = form['subject_list'].value()
            new1 = get_object_or_404(Section, name=subject)
            new3 = Student.objects.filter(name=name)
            if new3.exists():
            	new = Student.objects.get(name=name)
            	new1 = Enrollment(student=new, section= new1)
            	new1.save()
            	sect = Enrollment.objects.all()
            	form = SearchForm()
            	return render(request, 'exer3/student.html', {'sect': sect})
            else:
            	new = Student.objects.create(name=name)
            	new1 = Enrollment.objects.create(student=new, section= new1)
            	new1.save()
            	sect = Enrollment.objects.all()
            	form = SearchForm()
            	return render(request, 'exer3/student.html', {'sect': sect})

def add2(request):
    if request.POST:
        form = SubAdd()
        return render(request, 'exer3/add2.html', {'form': form})

def add3(request):
    if request.method == 'POST':
        form = SubAdd(request.POST)
        if form.is_valid():
            name = form['name'].value()
            new = Student.objects.create(name=name)
            new.save()
            first = Student.objects.all()
            form = SearchForm()
            return render(request, 'exer3/software.html', {'first': first, 'form': form})

def edit(request, pk):
    form = RegForm()
    edit1 = get_object_or_404(Enrollment, pk=pk) 
    edit = Student.objects.filter(name=edit1.student)
    return render(request, 'exer3/edit.html', {'edit1': edit1, 'edit': edit, 'form': form})

def edit1(request, pk):
    edit1 = get_object_or_404(Enrollment, pk=pk)
    edit = Student.objects.filter(name=edit1.student)
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():            
            name1 = form['name'].value()
            subject = form['subject_list'].value()
            new1 = get_object_or_404(Section, name=subject)  
            edit.delete()  
            new = Student.objects.create(name=name1)
            new1 = Enrollment.objects.create(student=new, section= new1)
            new1.save()
            sect = Enrollment.objects.all()
            form = SearchForm()
            return render(request, 'exer3/student.html', {'sect': sect})


def server_error(request):
    return render(request, 'errors/500.html')
 
def not_found(request):
    return render(request, 'errors/404.html')
 
def permission_denied(request):
    return render(request, 'errors/403.html')
 
def bad_request(request):
    return render(request, 'errors/400.html')