from rest_framework import serializers

class releaseGroupSerializer(serializers.Serializer):
    """
    Serialize the information related to the release groups
    """
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()
