from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ItemViewSet

router = SimpleRouter()
router.register(r'itens', ItemViewSet)

urlpatterns = router.urls
