from yandex import Yandex
from yandex_token import yandex_token

folder_name = 'vk_photo'

def test_folder_creation():
    result = (Yandex(folder_name, yandex_token)._create_folder(folder_name))
    assert result[0].status_code == 200
    assert result[1] == 'disk:/vk_photo'
    assert 'error' not in result