from rest_framework import serializers
from crud_with_apiviews.models import userlogin

class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userlogin
        fields = '__all__'

        
    def create(self, validated_data):
        return userlogin.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.f_name = validated_data.get('f_name', instance.f_name)
        instance.l_name = validated_data.get('l_name', instance.l_name)
        instance.DOB = validated_data.get('DOB', instance.DOB)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email_id = validated_data.get('email_id', instance.email_id)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.password = validated_data.get('password', instance.password)

        instance.save()
        return instance