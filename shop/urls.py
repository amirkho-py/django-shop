from django.urls import path
from . import views


app_name = "shop"
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:product_id>',views.detail,name='detail'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
