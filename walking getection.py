import numpy as np
import cv2
import os
import imutils

NMS_THRESHOLD=0.3
MIN_CONFIDENCE=0.2

blob = cv2.dnn.blobFrameImage(image, 1/255.0, (416, 416),
                                  swarpRB=True, crop=False)
model.setInput(blob)
layerOutputs = model.forward(layer_name)

boxes = []
centroids = []
confidences = []

for output in layerOutputs:
    for detection in outputs:
         scores = detection[5:]
         classID = np.argmax(scores)
         confidence = scores[classID]

         if classID == personidz and confidence > MIN_CONFIDENCE:
              box = detection[0:4] * np.array([W, H, W, H])
              (centerX, centerY, width, height) = box.astype("int")