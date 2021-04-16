from rest_framework import routers
from .views import OrdersViewSet


router = routers.DefaultRouter()

router.register(r"orders", OrdersViewSet, basename='orders')

urlpatterns = router.urls

