from django.urls import include, path
from .import views
from accounts import views as AccountView

urlpatterns = [
    path('', AccountView.vendorDashboard,name='vendor'),
    path('profile/',views.vprofile,name='vprofile'),
    path('menu-builder',views.menu_builder,name='menu_builder'),
    path('menu-builder/category/<int:pk>/',views.fooditems_by_category,name='fooditems_by_category'),
    
    
    #Category CURD
    path('menu-builder/category/add/',views.add_category,name='add_category'),
    path('menu-builder/category/edit/<int:pk>/',views.edit_category,name='edit_category'),
    path('menu-builder/category/delete/<int:pk>/',views.delete_category,name='delete_category'),
    
    #FoodItem CURD
    path('menu-builder/food/add/',views.add_food,name='add_food'),
]
