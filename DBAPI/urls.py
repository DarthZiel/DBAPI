from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drug.views import DrugViewSet
from user.views import UserViewSet,ProfileViewSet,PostitonViewSet,StructureViewSet
drug_router = routers.SimpleRouter()
drug_router.register(r'drug', DrugViewSet)
user_router = routers.SimpleRouter()
user_router.register(r'user', UserViewSet)

profile_router = routers.SimpleRouter()
profile_router.register(r'profile', ProfileViewSet)
position_router = routers.SimpleRouter()
position_router.register(r'position', PostitonViewSet)
structure_router = routers.SimpleRouter()
structure_router.register(r'structure', StructureViewSet)
urlpatterns = [
    path('api/',include(drug_router.urls)),
    path('api/', include(user_router.urls)),
    path('api/', include(position_router.urls)),
    path('api/', include(structure_router.urls)),
    path('api/', include(profile_router.urls)),
    # djoser urls
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('admin/', admin.site.urls),
    path('', include('drug.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)