from rest_framework import serializers
from .models import User, Manager, Intern

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['has_company_card']
