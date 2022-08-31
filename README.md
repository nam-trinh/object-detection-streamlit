# Object detection API using the transformers library from HuggingFace and FastAPI

## Introduction:

Object detection is the task of detecting an object in an image and drawing a bounding box around that object. This work is using DETR from Facebook AI Research with ResNet-50 for the task of object detection. Details of the model can be found at this paper "End-to-end object detection using transformers": https://arxiv.org/pdf/2005.12872.pdf

Official implementation of DETR at: https://github.com/facebookresearch/detr
## Instruction:

1. Install the requirements from requirements.txt:
```
pip install -r requirements.txt
```

2. Download model from Hugging Face at https://huggingface.co/facebook/detr-resnet-50/ or using git lfs to clone:
```
git lfs clone https://huggingface.co/facebook/detr-resnet-50/
```
If you have not installed git lfs yet, you have to install git lfs first.

Then, put the model file inside the folder detr-resnet-50/

3. Run the main.py to launch a FastAPI instance:
```
python main.py
```
The API will be at http://localhost:5000/object_detection/ 

4. Calling the API using a POST request: 
```
image_path = 'path/to/image'
headers = {"accept": "application/json"}
files = {'data': (image_path, open(image_path, 'rb'), "image/jpeg")}
response = requests.post(url=link_to_api, headers=headers, files=files)
```

Response will have the form: 
```
[{"cat":{"box":[283.5,118.16,1798.51,1115.62],"score":0.998}}]
```
where box will have the format: [xmin, ymin, width, height] and score is the probability showing how certain the object is.

5. Run streamlit:
```
streamlit run streamlit_object_detection.py
```

## Reference: 

1. "End-to-end object detection using transformers": https://arxiv.org/pdf/2005.12872.pdf
2. https://huggingface.co/facebook/detr-resnet-50/
3. https://github.com/aniketmaurya/tensorflow-fastapi-starter-pack