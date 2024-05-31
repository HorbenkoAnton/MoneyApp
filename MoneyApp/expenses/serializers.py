from rest_framework import serializers
from .models import Category, Expense

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Category
        fields = ['name' ,'owner']

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.HyperlinkedRelatedField(view_name='category-detail',queryset=Category.objects.all())
    class Meta:
        model = Expense
        fields = ['name' ,'amount','description', 'category','date','owner']

    def validate_category(self, value):
        request = self.context.get('request')
        if value.owner != request.user:
            raise serializers.ValidationError("You do not own this category.")
        return value
