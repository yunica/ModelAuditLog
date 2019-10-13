from django.contrib import admin
from django.urls import path
from Base.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', listar),
    path('add', agregar),
    path('update', modificar),

]
