from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/login/$', views.login, name='login'),
    #url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': 'login'}),
    url(r'', include('exer3.urls')),
]
#handler404 = 'exer3.views.not_found'
#handler500 = 'exer3.views.server_error'
#handler403 = 'exer3.views.permission_denied'
#handler400 = 'exer3.views.bad_request'