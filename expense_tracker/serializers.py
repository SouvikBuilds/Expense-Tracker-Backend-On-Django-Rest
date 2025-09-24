from .models import ExpenseModel
from rest_framework import serializers

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields = ['id','title','amount','category']
        read_only_fields = ['id']
    
    def create(self, validated_data):
        return super().create(validated_data)