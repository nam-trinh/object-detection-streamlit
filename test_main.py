from urllib import response
import requests
from PIL import Image
from io import BytesIO
import base64

def test_main(link_to_api, image_path):
    headers = {"accept": "application/json"}
    files = {'data': (image_path, open(image_path, 'rb'), "image/jpeg")}
    response = requests.post(url=link_to_api, headers=headers, files=files)
    return response


if __name__ == '__main__':
    path = "/Users/namtrinh/Desktop/cat.jpeg"
    response = test_main(link_to_api='http://127.0.0.1:5000/detect_object/', image_path=path)
    print(response.content)