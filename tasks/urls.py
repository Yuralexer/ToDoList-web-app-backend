from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

app_name = "task"
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="task")
urlpatterns = router.urls