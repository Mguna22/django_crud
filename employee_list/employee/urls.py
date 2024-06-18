from django.urls import path
from . import views
urlpatterns = [
    path('create', views.home, name='create'),
    path('upload', views.data_upload, name = 'upload'),
    path('list-of-employee/', views.list_of_employee, name= 'list_of_employee'),
    path('list-of-employee/detail/<int:id>/', views.detail_of_employee, name='detail_of_employee'),
    path('list-of-employee/detail/update/<int:id>/', views.update_data, name='update_data'),
    path('list-of-employee/detail/delete/<int:id>/', views.delete_data, name="delete_data"),













    # path('', views.index, name='main'),
    # path('employee_detail/<int:id>/', views.emp_details, name = 'dtl'),
    # path('form/', views.emp_form, name='form'),
    # path('<int:id>', views.del_id, name='del1'),
    # path('get_edit/<int:id>/', views.get_edt_id, name='get_edt'),
    # path('edit form/<int:id>/', views.edit, name='edit')
]