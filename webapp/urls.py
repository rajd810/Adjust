from django.urls import path, include
from . import views
from rest_framework import routers
from .views import get_adjust_data, import_db

router = routers.DefaultRouter()
router.register('webapp', views.WebappView)


urlpatterns = [
    path('', include(router.urls)),
    path('import_db/', import_db),
]
