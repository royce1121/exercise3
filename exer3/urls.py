from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.list, name='list'),
    path('Subject/<int:pk>/', views.subject, name='subject'),
    path('Student/List/', views.student, name='student'),
    path('Profile/', views.profile, name='profile'),
    path('Remove/<int:pk>/', views.remove, name='remove'),
    path('Remove/student/<int:pk>/', views.remove1, name='remove1'),   
    path('Edit/<int:pk>/', views.edit, name='edit'),
    path('New/', views.new, name='new'),
    path('Add/', views.add, name='add'),
    path('Add/subject', views.add2, name='add2'),
    path('Added/subject', views.add3, name='add3'),
    path('Add/Student/', views.add1, name='add1'),    
    path('Edited/<int:pk>/', views.edit1, name='edit1'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create, name='create'),
    path('search/subject', views.search1, name='search1'),
    path('list/', views.software, name='software'),
    #url(r'^account/$', views.login, name='login'),   
    #url(r'^logout/$', views.logout_view, name='logout_view'),
]