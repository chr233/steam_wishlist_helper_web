from django import urls
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from app import views
from rest_framework.authtoken.views import obtain_auth_token

visitor_router = routers.DefaultRouter()
visitor_router.register(r'games', views.GameSimpleInfoViewSet)
visitor_router.register(r'tags', views.TagViewSet)
visitor_router.register(r'companys', views.CompantViewSet)

admin_router = routers.DefaultRouter()
admin_router.register(r'games', views.GameFullInfoViewSet)
admin_router.register(r'tags', views.TagViewSet)
admin_router.register(r'companys', views.CompantViewSet)
admin_router.register(r'bans', views.GameBanListViewSet)
admin_router.register(r'adds', views.GameAddListViewSet)
admin_router.register(r'access', views.AccessStatsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('', include(visitor_router.urls)),
    path('adv/', include(admin_router.urls)),
    path('test', views.test)
]
