from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import BlotterEntry
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                return render(request, 'app/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('signup')

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

@method_decorator(login_required, name='dispatch')
class BlotterPageView(ListView):
    model = BlotterEntry
    template_name = 'app/list.html'
    context_object_name = 'entrys'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entries = BlotterEntry.objects.all()

        search_query = self.request.GET.get('search', '')
        if search_query:
            entries = entries.filter(name__icontains=search_query)

        context['entries'] = entries
        return context

class AddPageView(CreateView):
    model = BlotterEntry
    fields = ['name', 'address', 'description', 'date', 'contact_number']
    template_name = 'app/add.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditPageView(UpdateView):
    model = BlotterEntry
    fields = ['name', 'address', 'description', 'date', 'contact_number']
    template_name = 'app/edit.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeletePageView(DeleteView):
    model = BlotterEntry
    template_name = 'app/delete.html'
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entry'] = self.get_object() 
        return context
