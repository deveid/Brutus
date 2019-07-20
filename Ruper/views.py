from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,UpdateView
from .models import *
from .forms import ShoppingItemForm,ShoppingListForm
from django.urls import reverse_lazy
# Create your views here.

def register_view(request):
    register_form=RegisterForm()
    if request.method=="POST":
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            save_user=register_form.save()
            return redirect("Ruper:cart")
        else:
            register_form=RegisterForm()
    context={}
    context['rForm']=RegisterForm()
    return render (request,'index.html', context)

def cart_view(request):
    return render(request,'cart.html')


