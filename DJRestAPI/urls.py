from django.conf.urls import url, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^', include('djwebapp.urls')),
]
