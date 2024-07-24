from django.urls import path
from . import views

urlpatterns = [
    path('investor/', views.create_investor, name='create_investor'),
    path('investors/', views.list_investors, name='list_investors'),
    path('investor/<int:id>/', views.get_investor_by_id_view, name='get_investor_by_id'),
    path('investor/<int:id>/update/', views.update_investor_view, name='update_investor'),
    path('investor/<int:id>/delete/', views.delete_investor_view, name='delete_investor'),

]
