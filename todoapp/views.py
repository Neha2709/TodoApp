from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect 
from django.db.models import Q



# Create your views here.
def todoappView(request):
    # all_items = TodoItem.objects.all().filter(~Q(status='Completed'))
    all_items = TodoItem.objects.filter(~Q(status='Completed')).order_by('ETA')
    # not_started_items = TodoItem.objects.all().filter(status='Not Started')
    # in_progress_items = TodoItem.objects.all().filter(status='In progress')
    # completed_items = TodoItem.objects.all().filter(status='Completed')
    return render(request, 'todolist.html',{'all_items':all_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoItem(content = x, status = request.POST['status'], ETA = request.POST['ETA'])
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 

def deleteTodoView(request, i):
    y = TodoItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 

def changeStatus(request, i):
    y = TodoItem.objects.get(id= i)
    y.status = request.POST['status']
    y.save()
    return HttpResponseRedirect('/todoapp/') 

def filterByStatus(request):
    x = request.POST['status']
    if(x=='Completed'):
        items = TodoItem.objects.filter(status=x).order_by('-ETA')
    else:
        items = TodoItem.objects.filter(status=x).order_by('ETA')
    return render(request, 'todolist.html',{'all_items':items})