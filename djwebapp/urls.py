from django.conf.urls import url
import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^api/tutorials$', views.tutorial_detail),
    url(r'^api/tutorials/(?<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published)
    
]
