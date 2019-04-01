from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def homeView(request):
    return render(request, "app/base.html")

def aboutView(request):
    return render(request, "app/about.html")


def todoView(request):
    items = TodoItem.objects.all()
    context = {
        'items': items
    }
    return render(request, "app/todo.html", context)

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = c)
    new_item.save()

    return HttpResponseRedirect(reverse('todo-home'))

def deleteTodo(request, todo_id):
    item_delete = TodoItem.objects.get(id = todo_id)
    item_delete.delete()
    return HttpResponseRedirect(reverse('todo-home'))

