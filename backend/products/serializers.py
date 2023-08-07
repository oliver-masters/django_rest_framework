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
    related_products = ProductInLineSerializer(source="user.product_set.all", read_only=True, many=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # email = serializers.EmailField(source="user.email", write_only=True)

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
            "my_discount",
            "my_user_data",
            "related_products",
        ]

    def get_my_user_data(self, obj):
        return {"username": obj.user.username}


    # This is a simple way of doing validation, but validators.py is better

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("This title is already in use")
    #     return value


    # Example of how one could use an email for a one time event

    # def create(self, validated_data):
    #     email = validated_data.pop("email")
    #     print(email)
    #     obj = super().create(validated_data)
    #     return obj
    #
    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     print(email)
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        return obj.get_discount()
