from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.index, name='index'),
    path('blog/',views.blog, name='blog'),
    path('expression',views.expression, name="expression value")
]