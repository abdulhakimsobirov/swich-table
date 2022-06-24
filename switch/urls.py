from django.urls import path
from . import views

urlpatterns = [
    path('', views.SwitchList.as_view(), name='switch_list'),
    path('view/<int:pk>', views.SwitchDetail.as_view(), name='switch_view'),
    path('new', views.SwitchCreate.as_view(), name='create_switch'),
    path('edit/<int:pk>', views.SwitchUpdate.as_view(), name='edit_switch'),
    path('delete/<int:pk>', views.SwitchDelete.as_view(), name='delete_switch'),
    path('table-hower/', views.tableHower, name='table-hower')
]



