from django.shortcuts import render
import pyrebase
from django.contrib import auth

# Create your views here.

config = {
    "apiKey": "AIzaSyCIfGntwga6XKHOLWvFI24k_ZjzW6WFkdk",
    "authDomain": "arcloud-7e352.firebaseapp.com",
    "databaseURL": "https://arcloud-7e352-default-rtdb.firebaseio.com",
    "projectId": "arcloud-7e352",
    "storageBucket": "arcloud-7e352.appspot.com",
    "messagingSenderId": "836597662489",
    "appId": "1:836597662489:web:e6bd2531dc693d9d44bb88",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def indexView(request):
    return render(request,'index.html')

def PostSubscriberView(request):
    email=request.POST.get('email')
    data = {"email":email}
    database.child('subscribers').child('users').push(data)
    return render(request,"welcome.html")

def PostFeedbackView(request):
    name=request.POST.get('name')
    email=request.POST.get('mail')
    feedback=request.POST.get('feedback')
    print(name,email,feedback)
    data = {"name":name,"email":email,"feedback":feedback}
    database.child('feedback').child('users').push(data)
    return render(request,"index.html")

def welcomeView(request):
    return render(request,'welcome.html')