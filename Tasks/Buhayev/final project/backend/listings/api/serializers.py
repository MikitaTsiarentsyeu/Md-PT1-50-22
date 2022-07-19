from rest_framework import serializers

from listings.models import Listing 

class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    seller_username = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()
    
    def get_country(self, obj): return 'England'
    
    def get_seller_username(self, obj): return obj.seller.username
    
    def get_seller_agency_name(self, obj): return obj.seller.profile.agency_name
    
    class Meta:
        model = Listing
        fields = '__all__'