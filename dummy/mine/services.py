from .models import Developer, TeamDeveloperMap
import requests
from dummy.settings import ALERT_BASE_URL, ALERT_TOKEN_KEY
from .exceptions import ParseException
from .errors import BAD_REQUEST


class MineService:

    @staticmethod
    def get_developer(**kwargs):
        developer_object, _ = Developer.objects.get_or_create(**kwargs)
        return developer_object

    @staticmethod
    def get_team(id):
        try:
            return TeamDeveloperMap.objects.get(id=id)
        except TeamDeveloperMap.DoesNotExist:
            raise ParseException(BAD_REQUEST)

    @staticmethod
    def create_team(data):
        team_name = data.get('team', {}).get('name')
        developers = data.get('developers')
        developer_list = []
        for developer in developers:
            developer_name = developer.get('name')
            developer_number = developer.get('phone_number')
            developer = MineService.get_developer(name=developer_name, mobile=developer_number)
            developer_id = developer.id
            developer_list.append(developer_id)
        team_developer_map = TeamDeveloperMap.objects.create(team_name =team_name, developers=developer_list)
        return {"team_id": team_developer_map.id}

    @staticmethod
    def post_alert(team_id):
        team = MineService.get_team(team_id)
        developers = team.developers
        if len(developers):
            developer = MineService.get_developer(id=developers[0])
            data = {
                'phone_number': developer.mobile,
                'message': 'Too many 5xx!'
                }
            # log.push('Posting data for alert'+ data)
            MineService.post_alert_for_number(data)
        return {'status': 200, 'message': 'Sent'}


    @staticmethod
    def post_alert_for_number(data):
        try:
            # log.push('Received alertt' + data)
            url = ALERT_BASE_URL+ALERT_TOKEN_KEY
            response = requests.post(url=url, json=data)
            # log.push('Received response for ' + data+'which is '+ response.text)
            return
        except Exception as error:
            # log.push('Exception response for post alert ' + error)
            return