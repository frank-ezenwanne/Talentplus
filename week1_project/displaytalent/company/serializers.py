from rest_framework import serializers
from .models import Company

class PostCompanySerializer(serializers.ModelSerializer): #Converts incoming JSON to native python data types
    class Meta:
        model = Company
        fields = ('name','email')