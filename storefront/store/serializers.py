from decimal import Decimal
from gc import collect
from pyexpat import model
from rest_framework import serializers


from store.models import Collection, Product

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'collection', 'unit_price','price_with_tax']
        # fields = '__all__'
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
# #    collection = serializers.PrimaryKeyRelatedField(
# #        queryset = Collection.objects.all()
# #    )
# #    collection = serializers.StringRelatedField() 
# #    collection = CollectionSerializer()
    collection = serializers.HyperlinkedRelatedField(view_name='collection-detail', queryset =Collection.objects.all())
    
    def validate_empty_values(self, data):
        return super().validate_empty_values(data)
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def calculate_tax(self, product:Product):
       return product.unit_price * Decimal(1.3)
   
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    
   