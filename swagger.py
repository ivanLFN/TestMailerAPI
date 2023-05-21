from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="Рассылка API",
        default_version='v1',
        description="Описание API рассылки",
        contact=openapi.Contact(email="Ivan.Lozhkin2020@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)