from rest_framework import routers

from .api_views import ApplicationsViewSet

router = routers.SimpleRouter()
router.register(r'applications', ApplicationsViewSet)

urlpatterns = router.urls
