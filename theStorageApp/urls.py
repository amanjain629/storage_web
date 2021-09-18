from django.urls import path
from . import views

urlpatterns = [
    path("",views.indexView,name='index'),
    path("postSubscriber/",views.PostSubscriberView,name='postSubscriber'),
    path("welcome",views.welcomeView,name='welcome'),
    path("postFeedback/",views.PostFeedbackView,name='postFeedback'),
]