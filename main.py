from typing import Union
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from inference import predict, read_image
import uvicorn

app = FastAPI()

def plot_image(image, bounding_boxes):
    pass

@app.get('/')
def get_root():
    return {'message': 'Welcome to object detection API using DETR from Facebook AI Research!'}

@app.post('/detect_object/')
async def predict_api(data: UploadFile = File(...)):

    extension = data.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    print(data.filename)
    if not extension:
        return "Image must be jpg, jpeg or png format!"
    image = read_image(await data.read())
    prediction = predict(image)
    return prediction

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")