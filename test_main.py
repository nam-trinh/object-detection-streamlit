import requests
from PIL import Image
from io import BytesIO
def test_main(link_to_api, image):
    headers = {"accept": "application/json"}
    files = {'data': image}
    requests.post(url=link_to_api, headers=headers, files=files)


if __name__ == '__main__':
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = BytesIO(Image.open(requests.get(url, stream=True).raw))

    test_main(link_to_api='http://127.0.0.1:5000/object_detection/', image=image)