from . import views
from django.urls import path
from .forms import ContactForm
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog1'

urlpatterns = [
    path("",views.PostList.as_view(), name ="index"),
    path('about/', views.about, name='about'),
    path("contact/",views.ContactForm_view, name="contact"),
    path('get-started/', views.get_started, name='get_started'),
    path("search/", views.search_results, name="search"),
    path("<slug:slug>/",views.PostDetail.as_view(), name ="details"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)