# import debug_toolbar
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from app import views
from rest_framework.authtoken.views import obtain_auth_token

visitor_router = DefaultRouter()
visitor_router.register(r'games', views.GameSimpleInfoViewSet, 'A')
visitor_router.register(r'tags', views.TagViewSet, 'A')
visitor_router.register(r'companys', views.CompantViewSet, 'A')

admin_router = DefaultRouter()
admin_router.register(r'games', views.GameFullInfoViewSet, 'B')
admin_router.register(r'tags', views.TagViewSet, 'B')
admin_router.register(r'companys', views.CompantViewSet, 'B')
admin_router.register(r'bans', views.GameBanListViewSet, 'B')
admin_router.register(r'adds', views.GameAddListViewSet, 'B')
admin_router.register(r'access', views.AccessStatsViewSet, 'B')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('', include(visitor_router.urls)),
    path('adv/', include(admin_router.urls)),
    # path('test', views.test),
    # path('__debug__/', include(debug_toolbar.urls))
]
