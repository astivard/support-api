from django.urls import include, path

from rest_framework_nested import routers as nested_routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from support.views import (MessageViewSet, TicketViewSet,
                           UserRegistrationViewSet)

ticket_router = nested_routers.DefaultRouter()
ticket_router.register(r'tickets', TicketViewSet, basename='tickets')

message_router = nested_routers.NestedDefaultRouter(ticket_router, r'tickets', lookup='ticket')
message_router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('api/v1/', include(ticket_router.urls)),
    path('api/v1/', include(message_router.urls)),
    path('api/v1/registration/', UserRegistrationViewSet.as_view({'post': 'create'})),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
