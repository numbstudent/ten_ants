from django.urls import path

# from . import views
from tenants import views

urlpatterns = [
    path('hokage', views.defaultpage),
    path('master-unit', views.add_unit, name="master-unit"),
    path('delete-unit/<int:id>', views.delete_unit, name="delete-unit"),
    path('edit-unit/<int:id>', views.delete_unit, name="edit-unit"),
    path('master-product', views.add_products, name="master-product"),
    path('delete-product/<int:id>', views.delete_product, name="delete-product"),
    path('edit-product/<int:id>', views.edit_product, name="edit-product"),
]
