from rest_framework import serializers
from .models import Books  # Ensure this matches the model name

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'