from .models import ExpenseModel
from rest_framework_mongoengine import serializers

class ExpenseSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ExpenseModel
        fields = ['id', 'title', 'amount', 'category']
        read_only_fields = ['id']
    
    def create(self, validated_data):
        return super().create(validated_data)