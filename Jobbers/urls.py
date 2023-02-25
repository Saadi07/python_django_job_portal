
from django.contrib import admin
from django.urls import path, include
from jobs.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('blog/', include('django.contrib.auth.urls')),
    path('user/', include('user.urls'),)

]
