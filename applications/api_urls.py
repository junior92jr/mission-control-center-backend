from rest_framework import routers

from .api_views import ApplicationViewSet, ConfigurationViewSet

router = routers.SimpleRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'configurations', ConfigurationViewSet)

urlpatterns = router.urls
