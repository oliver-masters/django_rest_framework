from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Product
from .validators import validate_title_no_hello, unique_product_title


class ProductInLineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])

    class Meta:
        model = Product
        fields = [
            "owner",
            "pk",
            "url",
            "edit_url",
            "title",
            "content",
            "price",
            "sale_price",
            "public",
        ]

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
