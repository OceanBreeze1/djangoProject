from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from apps.forms import ProductForm
from apps.models import Product

# def home(request):
#     return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = "index.html"
class HomeView(TemplateView):
    template_name = "about.html"
class ContactView(TemplateView):
    template_name = "contact.html"
class MenuView(TemplateView):
    template_name = "menu.html"
class NewsView(TemplateView):
    template_name = "news.html"
class NewsdetailView(TemplateView):
    template_name = "news-detail.html"

