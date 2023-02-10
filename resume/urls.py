from django.urls import path,include
from resume.views import ProfileView
from django.conf.urls.static import static


urlpatterns = [
    path('upload/',ProfileView.as_view(), name='resume'),
    path('list/',ProfileView.as_view(), name='list')

]
