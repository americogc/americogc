from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import password_validation,authenticate
from core.models import Booking



class BookingsSerializer(serializers.Serializer):
    id_booking = serializers.ReadOnlyField()
    total = serializers.FloatField()
    check_in = serializers.DateField() 
    check_out = serializers.DateField() 
    customer_name = serializers.CharField()
    customer_lastname = serializers.CharField()
    customer_email = serializers.CharField()

    customer_tel = serializers.CharField()
    customer_special_req = serializers.CharField()
    option_pay = serializers.CharField()
    hour_arrive = serializers.CharField()

    estado = serializers.CharField()
    nro_personas = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def create(self, data):
        booking = Booking(**data)
        booking.save()
        return booking


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')
        
        self.context["user"] = user
        return data
        #pass

    def create(self,data):
        token,create = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
        