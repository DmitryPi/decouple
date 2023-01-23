from rest_framework import serializers

from decoup.billing.models import Invoice, ItemLine
from decoup.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]


class ItemLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLine
        fields = ["quantity", "description", "price", "taxed"]


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemLineSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ["user", "date", "due_date", "items"]

    def create(self, validated_data):
        items = validated_data.pop("items")
        invoice = Invoice.objects.create(**validated_data)
        for item in items:
            ItemLine.objects.create(invoice=invoice, **item)
        return invoice
