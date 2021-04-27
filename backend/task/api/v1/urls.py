from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet, TaskViewSet, RatingViewSet, TaskTransactionViewSet

router = DefaultRouter()
router.register("task", TaskViewSet)
router.register("tasktransaction", TaskTransactionViewSet)
router.register("rating", RatingViewSet)
router.register("message", MessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
