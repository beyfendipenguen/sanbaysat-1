from django.urls import path
from . import views

urlpatterns = [
 path("ürünGöster/<int:id>", views.ürünGöster, name="ürünGöster")
]