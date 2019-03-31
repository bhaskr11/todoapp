from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

# Create your views here.
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

    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_delete = TodoItem.objects.get(id = todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/todo/')

