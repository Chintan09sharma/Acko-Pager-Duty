from rest_framework import serializers
from .exceptions import ParseException
from .errors import BAD_REQUEST


class PostAlertSerializer(serializers.Serializer):
    """
    PostAlertSerializer
    """

    team_id = serializers.IntegerField(required=True, allow_null=False)

    def validate(self, data):
        try:
            team_id = data["team_id"]
        except KeyError:
            raise ParseException(BAD_REQUEST)
        return {"team_id": team_id}


class CreateTeamSerializer(serializers.Serializer):
    team = serializers.DictField(required=True, allow_null=False)
    developers = serializers.ListField(required=True, allow_null=False)

    def validate(self, data):
        try:
            team = data["team"]
            developers = data["developers"]
        except KeyError:
            raise ParseException(BAD_REQUEST)
        return {"team":team, "developers":  developers}
