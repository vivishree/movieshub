from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from app1.forms import moviesForm
from app1.models import movies1
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.forms import AuthenticationForm
def insert(request):
    obj=movies1.objects.all()
    return render(request,'app1/forms.html',{'data':obj})
       
class insert1(CreateView):
    model = movies1
    fields = '__all__'
    
    def get_initial(self):
       
        initial = super().get_initial()
        
       
        initial['name'] = 'Enter movie name.'
        initial['desc'] = 'Enter description.'
        initial['year'] = 2023  
        initial['genre'] = 'Enter genre.'
        return initial
    


class Cr(ListView):
    model=movies1
 
class update1(UpdateView):
    model = movies1
    form_class = moviesForm
    template_name = 'app1/movies1_form.html'
    success_url = reverse_lazy("list")
   

class delete1(DeleteView):
    model=movies1
    template_name='app1/delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_id'] = self.kwargs.get('pk') 
        return context
    success_url = reverse_lazy('list')
    
  
    

def HOME(request):
        return render(request,'app1/home.html')
def BASE1(request):
        return render(request,'app1/base.html')

def Signup(request):
    if request.user.is_authenticated:
        return render(request,'app1/home.html')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  

    else:
        form = UserCreationForm()
    return render(request, 'app1/signin.html', {'form': form})

def Logout(request):
     logout(request)
     return redirect('home')

def Login(request):
    
    if request.user.is_authenticated:
         return render(request,'app1/home.html')
    if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']
         user=authenticate(request,username=username,password=password)
         if user is not None:
                login(request,user)
                return redirect('home')
         else:
                msg='Error Login'
                form=AuthenticationForm(request.POST)
                return render(request,'app1/login.html',{'form':form,'msg':msg})
       
    else:
        form=AuthenticationForm()
        return render(request,'app1/login.html',{'form':form})