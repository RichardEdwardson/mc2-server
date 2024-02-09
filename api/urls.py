from rest_framework import routers
from .views import ClassroomView, ChatroomView

router = routers.DefaultRouter()
router.register('classrooms', ClassroomView)
router.register('chatroom', ChatroomView, basename='room')

urlpatterns = router.urls