from rest_framework import routers
from .views import ClassroomView, ChatroomView

router = routers.DefaultRouter(trailing_slash=False)
router.register('classrooms', ClassroomView)
router.register('chatroom', ChatroomView, basename='room')

urlpatterns = router.urls