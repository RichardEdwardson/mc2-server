from rest_framework import routers
from .views import ClassroomView, ChatroomView, ClassroomAssetView

router = routers.DefaultRouter(trailing_slash=False)
router.register('classroom', ClassroomView)
router.register('chatroom', ChatroomView, basename='room')
router.register('classroom_asset', ClassroomAssetView, basename='asset')

urlpatterns = router.urls