from rest_framework import serializers

class releaseGroupSerializer(serializers.Serializer):
    """
    Serialize the information related to the release groups
    """
    id = serializers.UUIDField()
    title = serializers.CharField()
    year = serializers.IntegerField()
    release_count = serializers.IntegerField()


class albumTypeReleaseGroupSerializer(serializers.Serializer):
    """
    Serialize the information related to the release groups of
    type album
    """

    albums = releaseGroupSerializer(many = True)
    next_offset = serializers.IntegerField()
    showing = serializers.CharField()
    release_group_count = serializers.IntegerField()
    date = serializers.DateTimeField()
