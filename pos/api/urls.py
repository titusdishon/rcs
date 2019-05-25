from django.urls import path
from .views import (
    NewParkingCreateView
)

app_name = "api"

urlpatterns = [
    # path('', ShopListAPIView().as_view(), name='Shop-list'),
    # path('<int:pk>/', ShopDetailsView.as_view(), name='detail'),
    # path('Shop/new/',ShopCreateView.as_view(), name='Shop-form'),
    # path('<int:pk>/update/', ShopUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', ShopDeleteView.as_view(), name='delete'),
    path('create/', NewParkingCreateView.as_view(), name='create'),
    # path('user/<str:username>',UserShopListView.as_view(), name='user-Shops'),
    # path('about/', views.about, name='products-about'),
]
