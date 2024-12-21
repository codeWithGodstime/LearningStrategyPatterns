from rest_framework import routers
from .views import ProgramViewset


router = routers.DefaultRouter()
router.register("", ProgramViewset, basename="programs")

urlpatterns = router.urls