from django.core.mail import send_mail,BadHeaderError
from django.views import generic
from .models import Post
from . import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    feedbackForm = forms.FeedbackForm()
    if request.method == 'POST':
        feedbackForm = forms.FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            feedbackForm.save()
            return render(request, 'index.html')
    return render(request, 'index.html',{'feedbackForm':feedbackForm})
def products(request):
    return render(request,'product.html')
def contact(request):
    return render(request,'contact.html')
def partners(request):
    return render(request,'partners.html')
def service(request):
    return render(request,'services.html')
class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by("-created_on")
    template_name = "updates.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
