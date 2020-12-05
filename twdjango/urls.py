from django.contrib import admin
from django.urls import path
from api_consumer import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('init/', v.init_view),
    path('seeing_data/', v.seeing_space_data),
    path('name/',v.name),
]
