from django.urls import path, include
from .views import GameViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('games', GameViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls))

]