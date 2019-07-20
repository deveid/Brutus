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


class DashboardView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name='dashboard.html'
    form_class=ShoppingListForm
    success_url=reverse_lazy(Ruper:dashboard)
    success_message="Shopping list created"

    def render_to_response(self, context, **response_kwargs):
        context['shopping_cart']=ShoppingList.objects.filter(owner=self.request.user)
        return super(DashboardView,self).render_to_response(context, **response_kwargs)

    def form_valid(self,form):
        list_name=form.get_cleaned('name')
        cart_owner=self.request.user
        if ShoppingList.objects.filter(name=list_name,owner=cart_owner).exists():
            form._errors['shopping list already exist']=''
            return super(DashboardView,self).form_invalid(form)
        form.instance.owner=owner
        return super(DashboardView,self).form_valid(form)

class ShoppingListUpdate(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model=ShoppingList
    form_class=ShoppingListForm
    template_name="Ruper/edit_this_form.html"
    success_url=reverse_lazy('Ruper:dashboard')
    success_message="Update was Successful"
    
    def form_valid(self,form):
        list_name=form.get_cleaned_data('name')
        cart_owner=self.request.user
        list=ShoppingList.objects.filter(owner=cart_owner,name=list_name)
        if list.exists() and list.first().id != self.kwargs.get('pk'):
            form._errors['A shopping list with the name exists']=''
            context={'form':form}
            context['shopping_lists']=ShoppingList.objects.filter(owner=cart_owner)
            return render_to_response('Ruper:dashboard.html',context)
        return super(ShoppingListUpdate,self).form_valid(form)

