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

3. Run the main.py to launch a FastAPI instance:
```
python main.py
```
The API will be at http://localhost:5000/object_detection/ 


## Reference: 

1. "End-to-end object detection using transformers": https://arxiv.org/pdf/2005.12872.pdf
2. https://huggingface.co/facebook/detr-resnet-50/
3. https://github.com/aniketmaurya/tensorflow-fastapi-starter-pack