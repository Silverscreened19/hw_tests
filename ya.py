import requests


class YaDisk:
    host = 'https://cloud-api.yandex.net'
    with open('/Users/silverscreened19/Documents/ya_disk_token.txt', 'r') as file:
        token_ya = file.readline()

    def __init__(self, token_ya):
        self.token = token_ya
        self.folder_name = 'Testing_hw'

    def headers(self):
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        return headers

    def create_folder(self):
        path = f'{self.folder_name}'
        url = f'{self.host}/v1/disk/resources?path={path}'
        response = requests.put(url, headers=self.headers())
        return response.status_code
        # if response.status_code == 201:
        #     link = response.json()['href']
        #     return link.split('=')[1]
        # else:
        #     print(response.json())


with open('/Users/silverscreened19/Documents/ya_disk_token.txt', 'r') as file:
    token_ya = file.readline()
yadisk = YaDisk(token_ya)
# print(yadisk.create_folder())
