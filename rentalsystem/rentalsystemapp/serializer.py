from rest_framework import serializers
from rentalsystemapp .models import Driver
from rentalsystemapp .models import Customer


class CustomerSerializers(serializers.ModelSerializer):
    customer_name=serializers.CharField(source="name", error_messages={"blanks":"Name cannot be blanks"})
    customer_address = serializers.CharField(source="address", error_messages={"blanks":"address cannot be blanks"})
    # custsomer_picture=serializers.ImageField(source="picture", error_messages={"blanks":"file cannot be blanks"})
    customer_mobile_number=serializers.CharField(source="mobile_number", error_messages={"blanks":"mobile_number cannot be blanks"})
    
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
    class Meta:
        model=Customer
        fields=["customer_name","customer_address", "customer_mobile_number"]
    
    
# class dSerializers(serializers.ModelSerializer):
#     customer_name=serializers.CharField(source="name", error_messages={"blanks":"Name cannot be blanks"})
#     customer_address = serializers.CharField(source="address", error_messages={"blanks":"address cannot be blanks"})
#     custsomer_picture=serializers.ImageField(source="picture", error_messages={"blanks":"mobile_number cannot be blanks"})
#     customer_mobile_number=serializers.CharField(source="mobile_number", error_messages={"blanks":"mobile_number cannot be blanks"})
    
#     def create(self, validated_data):
#         return Customer.objects.create(**validated_data)