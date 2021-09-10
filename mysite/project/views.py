from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted': 'August 11, 2021'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted': 'August 12,2021'

    }
]


def home(request):
    return render(request,'blog/home.html')
def about(request):
   return render(request,'blog/about.html',{'title':'about'})
def features(request):
     return render(request,'blog/features.html',{'title':'features'})
def signin(request):
    return render(request,'blog/signin.html',{'title':'signin'})
def register(request):
    return render(request,'blog/register.html',{'title':'register'})
def contact(request):
    return render(request,'blog/contact.html',{'title':'contact'})
# Create your views here.
