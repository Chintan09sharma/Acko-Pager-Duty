from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from .services import MineService
from .exceptions import ParseException
from .errors import BAD_REQUEST
from .serializers import PostAlertSerializer, CreateTeamSerializer


class MineView(GenericViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "post"]

    @action(
        methods=["post"], detail=False, authentication_classes=[], permission_classes=[]
    )
    def create_team(self, request):
        serializer = CreateTeamSerializer(data=request.data)
        if serializer.is_valid() is False:
            raise ParseException(BAD_REQUEST, errors=serializer.errors)
        validated_data = serializer.validated_data
        response = MineService.create_team(validated_data)
        return Response(response)

    @action(
        methods=["post"], detail=False, authentication_classes=[], permission_classes=[]
    )
    def post_alert(self, request):
        # log.push(request.data)
        serializer = PostAlertSerializer(data=request.data)
        if serializer.is_valid() is False:
            # log.push('Serializer ereror found')
            # log.push(request.data)
            raise ParseException(BAD_REQUEST, errors=serializer.errors)
        validated_data = serializer.validated_data
        response = MineService.post_alert(team_id = validated_data.get('team_id'))
        return Response(response)
