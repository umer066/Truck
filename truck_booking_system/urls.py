from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drivers.urls')),  # Include drivers app URLs
    path('api/', include('compliance.urls')), # Include compliance app URLs
    path('api/', include('notifications.urls')),  # Include notifications app URLs
    path('api/', include('monitoring.urls')),  # Include monitoring app URLs
    path('api/', include('booking.urls')),  # Include booking app URLs
    path('api/users/', include('users.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include('trucks.urls')),  # Include truck URLs
    path('api/', include('tracking.urls')),  # Include tracking URLs
]
