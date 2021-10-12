from django.conf.urls import url
from djwebapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^api/djwebapp$', views.tutorial_list),
    url(r'^api/djwebapp/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/djwebapp/published$', views.tutorial_list_published)
    
]
