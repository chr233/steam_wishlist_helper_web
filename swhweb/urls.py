from django import urls
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from app import views
from rest_framework.authtoken.views import obtain_auth_token

visitor_router = routers.DefaultRouter()
visitor_router.register(r'games', views.GameInfoViewSet)
visitor_router.register(r'tags', views.TagViewSet)
visitor_router.register(r'companys', views.CompantViewSet)

admin_router = routers.DefaultRouter()
admin_router.register(r'companys', views.CompantViewSet)
admin_router.register(r'tags', views.TagViewSet)
admin_router.register(r'companys', views.CompantViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(visitor_router.urls)),
    path('adv/', include(admin_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('test', views.test)
]
