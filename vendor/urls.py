from django.urls import include, path
from .import views
from accounts import views as AccountView

urlpatterns = [
    path('', AccountView.vendorDashboard,name='vendor'),
    path('profile/',views.vprofile,name='vprofile'),
    path('menu-builder',views.menu_builder,name='menu_builder'),
]
