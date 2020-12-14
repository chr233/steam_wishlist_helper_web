from django.urls import include, path
from rest_framework import routers
from app import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'games', views.GameInfoViewSet)
router.register(r'tags', views.TagsViewSet)
router.register(r'company', views.CompantViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token)
]
