from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from .pagination import (
    ShopLimitOffsetPagination,
    ShopPageNumberPagination, )
from rest_framework.permissions import (
    # AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    # IsAdminUser
)
from pos.models import VehicleParking
from .serializers import (
  ParkingSerializers
)
from .permissions import IsOwnerOrReadOnly


# class ShopListAPIView(ListAPIView):
#     # queryset = Shop.objects.all()
#     serializer_class = ParkingSerializers
#     pagination_class = ShopPageNumberPagination
#
#     def get_queryset(self, *args, **kwargs):
#         query_list = Shop.objects.all()
#         query = self.request.GET.get("q")
#         if query:
#             query_list = query_list.filter(
#                 Q(title__icontains=query)|
#                 Q(content__icontains=query)|
#                 Q(author__icontains=query)
#             ).distinct()
#         return query_list
#
#
# class ShopDetailsView(RetrieveAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopDetailSerializers
#     lookup_url_kwarg = "pk"
#
#
# class ShopUpdateView(RetrieveUpdateAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopUpdateView
#     permission_classes = [
#         IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
#     ]
#
#
# class ShopDeleteView(DestroyAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopDeleteSerializers
#     lookup_url_kwarg = "pk"


class NewParkingCreateView(CreateAPIView):
    queryset = VehicleParking.objects.all()
    serializer_class = ParkingSerializers
    permission_classes = [
        IsAuthenticated
    ]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, title="MY TITLE")
