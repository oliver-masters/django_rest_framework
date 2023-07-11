from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")

    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "email",
            "pk",
            "url",
            "edit_url",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    def create(self, validated_data):
        email = validated_data.pop("email")
        print(email)
        obj = super().create(validated_data)
        return obj

    def update(self, instance, validated_data):
        email = validated_data.pop("email")
        print(email)
        return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        return obj.get_discount()
