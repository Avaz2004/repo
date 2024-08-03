import requests

class Yandex:
    def __init__(self, folder_name, token):
        self.token = token
        self.url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        self.headers = {'Authorization': self.token}
        self.folder = self._create_folder(folder_name)

    def _create_folder(self, folder_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': folder_name}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            requests.put(url, headers=self.headers, params=params)
            print(f'Папка {folder_name} успешно создана.\n')
        else:
            print(f'Папка {folder_name} уже существует. Файлы с одинаковыми именами не будут скопированы.\n')
        response2 = requests.get(url, headers=self.headers, params=params)
        response3 = response2.json()['path']
        return response2, response3