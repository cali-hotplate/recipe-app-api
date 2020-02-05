from django.urls import path, include

from rest_framework.routers import DefaultRouter

from media import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'media'

urlpatterns = [
    path('', include(router.urls))
]
