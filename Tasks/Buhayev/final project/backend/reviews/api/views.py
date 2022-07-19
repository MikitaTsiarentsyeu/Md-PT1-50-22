from .serializers import ReviewSerializer
from reviews.models import Review
from rest_framework import generics



    

class ReviewCreate(generics.CreateAPIView): 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewList(generics.ListAPIView): 
    queryset = Review.objects.all()
    serializer_class =ReviewSerializer
    
    
