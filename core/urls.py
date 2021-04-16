from rest_framework import routers
from .views import OrdersViewSet, LinesViewSet


router = routers.DefaultRouter()

router.register(r"orders", OrdersViewSet, basename='orders')
router.register(r"lines", LinesViewSet, basename='lines')

urlpatterns = router.urls

