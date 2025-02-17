from rest_framework import serializers


class SearchQuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=255)
    status = serializers.CharField(read_only=True)