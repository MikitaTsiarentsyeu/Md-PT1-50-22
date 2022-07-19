from rest_framework import serializers
from users.models import Profile
from listings.models import Listing
from listings.api.serializers import ListingSerializer

class ProfileSerializer(serializers.ModelSerializer):
    seller_listings = serializers.SerializerMethodField()
    
    def get_seller_listings(self, odj): 
        listings = Listing.objects.filter(seller=odj.seller)
        listing_serializer = ListingSerializer(listings, many=True)
        return listing_serializer.data
    
    class Meta:
        model = Profile
        fields = '__all__'