from . import views
from django.urls import path
from .forms import ContactForm
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("",views.PostList.as_view(), name ="index"),
    path("contact/",views.ContactForm_view, name="contact"),
    path("search/", views.search_results, name="search"),
    path("<slug:slug>/",views.PostDetail.as_view(), name ="details"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)