from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('expenses/',views.get_all_expenses,name='get_all_expenses'),
    path('expenses/add/',views.add_expense,name='add_expense'),
    path('expenses/<int:pk>/edit/',views.edit_expense,name='edit_expense'),
    path('expenses/<int:pk>/delete/',views.delete_expense,name='delete_expense'),
    
]
