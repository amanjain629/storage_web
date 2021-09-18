from django.shortcuts import render
import pyrebase
from django.contrib import auth

# Create your views here.

config = {
    "apiKey": "AIzaSyCrk_8dwpcXurAz-oa5QGohs2On8Fk_2xs",
    "authDomain": "storagesystem-83746.firebaseapp.com",
    "databaseURL": "https://storagesystem-83746-default-rtdb.firebaseio.com",
    "projectId": "storagesystem-83746",
    "storageBucket": "storagesystem-83746.appspot.com",
    "messagingSenderId": "590468774618",
    "appId": "1:590468774618:web:22824e72ba86ec170683e3",
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
    data = {"name":name,"email":email,"feedback":feedback}
    database.child('feedback').child('users').push(data)
    return render(request,"index.html")

def welcomeView(request):
    return render(request,'welcome.html')