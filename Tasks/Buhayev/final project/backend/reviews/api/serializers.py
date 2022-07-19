from rest_framework import serializers

from reviews.models import Review 

class ReviewSerializer(serializers.ModelSerializer):
    review = serializers.CharField(max_length=2000)
    class Meta:
        model = Review
        fields = '__all__'