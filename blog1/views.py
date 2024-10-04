from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from .models import Post
from .models import Contact
from .forms import ContactForm, SearchForm
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

#def index(request):
    #return render(request, 'blog1/base.html')

#def base(request):
    #return render(request, 'blog1/index.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog1/index.html'
    paginate_by = 6

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog1/details.html'

def ContactForm_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
    else:
         form = ContactForm()
    return render(request, 'blog1/contact.html', {'form':form})

def search_results(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            try:
                search_query = form.cleaned_data['search_query']
                posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
                return render(request, 'blog1/search_results.html', {'posts': posts, 'search_query': search_query})
            except Exception as e:
                messages.error(request, 'Error sending message: {}'.format(e))
        else:
            form = SearchForm()
    return render(request, 'blog1/search_results.html', {'form': form})


# Utility function to render templates with common context
def render_template(request, template_name, context=None):
    if context is None:
        context = {}
    return render(request, template_name, context)


# Utility function to handle form errors
def handle_form_errors(form, request):
    messages.error(request, 'Form errors: {}'.format(form.errors))
    return render_template(request, 'blog1/contact.html', {'form': form})
