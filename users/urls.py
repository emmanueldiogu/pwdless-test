from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserView

router = SimpleRouter()

# router.register('user', UserView)

urlpatterns = [
    # path('user', include(router.urls)),
    path('user/', UserView.as_view())
]
