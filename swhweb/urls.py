
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from app import views
from rest_framework.authtoken.views import obtain_auth_token

from django.conf import settings

DEBUG = settings.DEBUG

router = DefaultRouter()
router.register(r'games', views.GameSimpleInfoViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'companys', views.CompantViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


if DEBUG:
    import debug_toolbar
    router.register(r'adv/games', views.GameFullInfoViewSet)
    router.register(r'adv/tags', views.TagViewSet)
    router.register(r'adv/companys', views.CompantViewSet)
    router.register(r'adv/bans', views.GameBanListViewSet)
    router.register(r'adv/adds', views.GameAddListViewSet)
    router.register(r'adv/access', views.AccessStatsViewSet)

    urlpatterns = [
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('api-token-auth/', obtain_auth_token),
        path('test', views.test),
        path('__debug__/', include(debug_toolbar.urls)),
        path('', include(router.urls)),
    ]
else:
    urlpatterns = [
        path('', include(router.urls)),
    ]
