from rest_framework.serializers import \
    (ModelSerializer,
     HyperlinkedIdentityField,
     SerializerMethodField
     )
from pos.models import VehicleParking, BusparkMatatu, BusparkSacco


class ParkingSerializers(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="api:detail",
        lookup_field="pk"
    )
    # delete_url = HyperlinkedIdentityField(
    #     view_name="Shop-api:delete",
    #     lookup_field="pk"
    # )
    update_url = HyperlinkedIdentityField(
        view_name="api:update",
        lookup_field="pk"
    )
    # turn the author into author name
    author = SerializerMethodField()

    class Meta:
        model = VehicleParking
        fields = [
            'citizen',
            'parking_category',
            'parking_subcategory',
            'buspark_matatu',
            'sticker_number',
            'number_plate',
            'sub_county',
            'ward',
            'zone',
            'sticker_collected',
        ]

    def get_author(self, obj):
        return str(obj.author.username)

#
# class ShopDetailSerializers(ModelSerializer):
#     author = SerializerMethodField()
#     avatar = SerializerMethodField()
#
#     class Meta:
#         model = Shop
#         fields = [
#             'citizen',
#             'parking_category',
#             'parking_subcategory',
#             'buspark_matatu',
#             'sticker_number',
#             'number_plate',
#             'ward',
#             'zone',
#
#         ]
#
#     def get_author(self, obj):
#         return str(obj.author.username)
#
#     def get_avatar(self, obj):
#         try:
#             avatar =obj.author.profile.image.url
#         except:
#             avatar=None
#         return avatar
#
#
# class ShopUpdateView(ModelSerializer):
#     class Meta:
#         model = Shop
#         fields = [
#             'id',
#             'title',
#             'content',
#             'date_modified',
#             'author',
#         ]
#
#
# class ShopCreateSerializers(ModelSerializer):
#     class Meta:
#         model = Shop
#         fields = [
#             'id',
#             'title',
#             'content',
#             'date_modified',
#             'author',
#         ]
#
#
# class ShopDeleteSerializers(ModelSerializer):
#     class Meta:
#         model = Shop
#         fields = [
#             # 'id',
#             'title',
#             'content',
#             'date_modified',
#             'author',
#         ]


