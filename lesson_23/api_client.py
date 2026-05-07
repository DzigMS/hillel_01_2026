from uuid import UUID

import requests

from model import DemoQaUser, ErrorResponseAccount

BOOKSTORE_ENDPOINT = 'BookStore'
URL_PATTERN = '{protocol}://{host}/{path}/{api_version}/{endpoint}'

class AccountEndpoints:
    PATH = 'Account'
    REGISTER = 'User'
    GENERATE_TOKEN = 'GenerateToken'
    AUTHORIZED = 'Authorized'
    USER = 'User'



class APIClient:
    def __init__(self, **kwargs):
        self.protocol = kwargs.get('protocol', 'https')
        self.host = 'demoqa.com'
        self.api_version = 'v1'

    def get_request(self, path, endpoint):
        return requests.get(
            url=URL_PATTERN.format(
                protocol=self.protocol,
                host=self.host,
                api_version=self.api_version,
                path=path,
                endpoint=endpoint
            ),
            headers=self.headers(),
        )

    def post_request(self, path, endpoint, data):

        return requests.post(
            url=URL_PATTERN.format(
                protocol=self.protocol,
                host=self.host,
                api_version=self.api_version,
                path=path,
                endpoint=endpoint
            ),
            headers=self.headers(),
            json=data,
        )

    def put_request(self):
        pass

    def delete_request(self):
        pass

    @staticmethod
    def headers():
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }


class DemoQAClient(APIClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def _map_response_object(response, model_class):
        resp_data = response.json()
        print(f'resp_data = {resp_data}')
        print(f'resp status = {response.status_code}')
        if response.status_code in [400, 401, 402, 403, 404, 406]:
            return ErrorResponseAccount(**resp_data)
        elif model_class == bool and isinstance(resp_data, bool):
            return resp_data
        return model_class(**resp_data)


    def post_account_request(self, user, endpoint, model_class):
        user_data = {
            "userName": user.name,
            "password": user.password,
        }
        resp = self.post_request(endpoint=endpoint, path=AccountEndpoints.PATH, data=user_data)
        return self._map_response_object(resp, model_class)

    def register_user(self, user: DemoQaUser):
        return self.post_account_request(user, AccountEndpoints.REGISTER, DemoQaUser)

    def is_authorized_user(self, user: DemoQaUser): #typehint
        return self.post_account_request(user, AccountEndpoints.AUTHORIZED, bool)

    def get_user(self, user):
        endpoint = AccountEndpoints.USER + '/' + user.user_id
        resp = self.get_request(path=AccountEndpoints.PATH, endpoint=endpoint)
        return self._map_response_object(resp, DemoQaUser)


