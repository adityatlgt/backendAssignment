
from rest_framework.routers import DefaultRouter
from .views import *

# Urls map to view functions.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls