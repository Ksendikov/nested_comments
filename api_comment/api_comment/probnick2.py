from rest_framework import serializers

level = serializers.SerializerMethodField('get_level')

print(type(level))
def get_level(self, obj):
    obj = self.obj
    return obj

print(level)