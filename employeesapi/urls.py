from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from employeesapi.employeesapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeesViewSet, base_name='employees')

urlpatterns = (
    url(r'employees', views.EmployeesViewSet),
)

urlpatterns = format_suffix_patterns(urlpatterns)

