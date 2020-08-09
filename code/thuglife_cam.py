"""
    @author: Miguanyu
"""
import cv2
from PIL import Image
import numpy as np
import time



maskPath = "mask.png"
cascPath = "123.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

mask = Image.open(maskPath)

def thug_mask(image):


	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, 1.15)

	background = Image.fromarray(image)

	for (x,y,w,h) in faces:

		resized_mask = mask.resize((w,h), Image.ANTIALIAS)
		offset = (x,y)

		background.paste(resized_mask, offset, mask=resized_mask)


	return np.asarray(background)

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)


while True:
	ret, frame = cap.read()
	if ret == True:
          gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          faces = faceCascade.detectMultiScale(gray, 1.15)
          background = Image.fromarray(frame)
          for (x,y,w,h) in faces:       
		      resized_mask = mask.resize((w,h), Image.ANTIALIAS)
		      offset = (x,y)
		      background.paste(resized_mask, offset, mask=resized_mask)
          frame=np.asarray(background)
          cv2.imshow('Live',frame)

          if cv2.waitKey(1)==27:
              break

cap.release()

cv2.destroyAllWindows()
