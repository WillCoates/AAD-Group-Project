from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="staffmodule-home"),
    path('products', views.products, name="staffmodule-products"),
    path('reports', views.reports, name="staffmodule-reports"),
    path('sales', views.sales, name="staffmodule-sales"),
    path('intelligence', views.intelligence, name="staffmodule-intelligence"),
    path('admin', views.admin, name="staffmodule-admin"),
    path('createcustomer', views.createCustomer, name="staffmodule-createCustomer"),
    path('createstaff', views.createStaff, name="staffmodule-createStaff")
    # path('add', views.add, name="staffmodule-add"),
]
