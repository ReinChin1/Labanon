from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import BlotterEntry
from .forms import BlotterEntryForm

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlotterPageView(TemplateView):
    template_name = 'app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entries = BlotterEntry.objects.all()

        search_query = self.request.GET.get('search', '')
        if search_query:
            entries = entries.filter(name__icontains=search_query)

        context['entries'] = entries
        return context

class AddPageView(TemplateView):
    template_name = 'app/add.html'

    def get(self, request, *args, **kwargs):
        form = BlotterEntryForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = BlotterEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return self.render_to_response({'form': form})
