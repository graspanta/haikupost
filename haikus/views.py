from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import HaikuCreateForm
from .models import Haiku
from django.db.models import Q
from django.contrib import messages


class HaikuListView(ListView):
    model = Haiku
    ordering = '-created_at'
    template_name = "haikus/haiku_list.html"
    paginate_by = 4
    

class HaikuDetailView(DetailView):
    model = Haiku
    context_object_name = 'haiku'
    template_name = "haikus/haiku_detail.html"

class HaikuCreateView(CreateView):
    model = Haiku
    template_name = "haikus/haiku_create.html"
    form_class = HaikuCreateForm
    success_url = reverse_lazy('haiku_list')
    
    def form_valid(self, form):
        haiku = form.save(commit=False)
        haiku.author = self.request.user
        haiku.save()
        messages.success(self.request, 'SUCCESS TO CREATE')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'FAILED')
        return super().form_invalid(form)
        
    

class SearchResultsListView(ListView):
    model = Haiku
    fields = ('poem', 'author', )
    context_object_name = 'haiku_list'
    template_name = "haikus/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Haiku.objects.filter(
            Q(poem__icontains=query)  | Q(author__username__icontains=query)
        )