import re
from unittest import result
from transformers import DetrFeatureExtractor, DetrForObjectDetection
import torch
from PIL import Image
from io import BytesIO

feature_extractor = DetrFeatureExtractor.from_pretrained("./detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("./detr-resnet-50")

def read_image(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

def predict(image):
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    # convert outputs (bounding boxes and class logits) to COCO API
    target_sizes = torch.tensor([image.size[::-1]])
    results = feature_extractor.post_process(outputs, target_sizes=target_sizes)[0]
    confident_results =[]
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        # keep detections with score > 0.9
        if score > 0.9:
            object = model.config.id2label[label.item()]
            confident_result = {object: {'box': box, 'score': round(score.item(), 3)}}
            confident_results.append(confident_result)
    return confident_results
    
if __name__ == '__main__':
    file = '/Users/namtrinh/Desktop/cat.jpeg'
    image = Image.open(file)
    confident_results = predict(image)
    print(confident_results)
        