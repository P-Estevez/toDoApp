from django.shortcuts import render,redirect
from .models import todoList
from .forms import todoListForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
	todoItems = todoList.objects.order_by('id')
	form = todoListForm()
	context = {'todoItems':todoItems,'form':form}
	return render(request,'todolist/index.html',context)

@require_POST
def addTodoItem(request):
	form = todoListForm(request.POST)
	if form.is_valid:
		newTodoItem= todoList(text=request.POST['text'])
		newTodoItem.save()
	return redirect('index')

def completedTodo(request,todoId):
	toDo = todoList.objects.get(pk=todoId)
	toDo.completed = True
	toDo.save()
	return redirect('index')

def deleteCompleted(request):
	todoList.objects.filter(completed__exact=True).delete()
	return redirect('index')

def deleteAll(request):
	todoList.objects.all().delete()
	return redirect('index')