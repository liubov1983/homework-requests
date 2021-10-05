import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'True'}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path):
        href = self._get_upload_link(file_path=file_path).get('href', '')
        response = requests.put(href, data=open('test.txt', 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл успешно загружен")

if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('test.txt')

    