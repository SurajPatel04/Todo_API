from django.urls import include, path
from .import views
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'test',api_view)

urlpatterns = [
    path("", views.test_view)
]


