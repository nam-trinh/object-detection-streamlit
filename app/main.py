from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_root():
    return {'message': 'Welcome to object detection API using Detr from Facebook AI Research!'}

@app.post('/object_detection')
def object_detection():



if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
