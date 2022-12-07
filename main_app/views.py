from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from main_app.models import Todo
# Create your views here.
def home(request):
    todos =Todo.objects.all().order_by('title')
    return render(request,'main_app/home.html',{'todos': todos})

def add(request):
    if request.method=='GET':
        return render(request, 'main_app/add.html')
    else:
        t=request.POST['title'] 
        d=request.POST['description']   
        Todo.objects.create(title=t, description=d, is_complete=False)
        return redirect('home')      

def delete(request,id):
    todo=Todo.objects.get(id=id).delete() 
    return redirect('home')   

def edit(request,id):
    try:
        todo=Todo.objects.get(id=id)
        if request.method=='GET':
            return render(request,'main_app/edit.html',{'todo':todo})
        else:
            title= request.POST['title']
            description=request.POST['description']   
            todo.title= title
            todo.description=description
            todo.save()
            return redirect('home')
    except:
        return HttpResponse('The object with that id doesnot exist')     

def delete_all(request):
    todo=Todo.objects.all().delete()
    return redirect('home')



  