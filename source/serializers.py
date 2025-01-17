from rest_framework import serializers

from source.models import Chicken, Egg


class ChickenSerializers(serializers.ModelSerializer):
    class Meta:
        model=Chicken
        fields='__all__'

class EggSerializers(serializers.ModelSerializer):
    chicken = serializers.PrimaryKeyRelatedField(queryset=Chicken.objects.all())
    class Meta:
        model = Egg
        fields = '__all__'
    def create(self, validated_data):
        Egg.objects.create(**validated_data)
        return Egg



