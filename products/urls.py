from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='products-home'),
    path('create', views.create, name='products-create'),
    path('<int:product_id>', views.details, name='products-details'),
    path('<int:product_id>/upvote', views.upvote, name='products-upvote')
]
