#!/usr/bin/python

import sys
import os
import time
import cv2
import numpy as np

print('\ndetect_er_chars.py')
print('       A simple demo script using the Extremal Region Filter algorithm described in:')
print('       Neumann L., Matas J.: Real-Time Scene Text Localization and Recognition, CVPR 2012\n')


if (len(sys.argv) < 2):
  print(' (ERROR) You must call this script with an argument (path_to_image_to_be_processed)\n')
  quit()

#pathname = os.path.dirname(sys.argv[0])
pathname='/Users/swati/opencv_contrib/modules/text/samples'
img  = cv2.imread(str(sys.argv[1]))
gray = cv2.imread(str(sys.argv[1]),0)
gray = cv2.resize(gray,(700,700))
img= cv2.resize(img,(700,700))
img = cv2.GaussianBlur(img,(15,15),0)
erc1 = cv2.text.loadClassifierNM1(pathname+'/trained_classifierNM1.xml')
er1 = cv2.text.createERFilterNM1(erc1)

erc2 = cv2.text.loadClassifierNM2(pathname+'/trained_classifierNM2.xml')
er2 = cv2.text.createERFilterNM2(erc2)

regions = cv2.text.detectRegions(gray,er1,er2)

#Visualization
rects = [cv2.boundingRect(p.reshape(-1, 1, 2)) for p in regions]
for rect in rects:
  cv2.rectangle(img, rect[0:2], (rect[0]+rect[2],rect[1]+rect[3]), (0, 0, 0), 2)
for rect in rects:
  cv2.rectangle(img, rect[0:2], (rect[0]+rect[2],rect[1]+rect[3]), (0, 255, 0), 1)
  '''
  print(rect[0:2])
  print('xxx1')
  print(rect[0]+rect[2],rect[1]+rect[3])
  print('xxx2')
  print(rect[0],rect[1],rect[2],rect[3])
  
   
  crop = img[rect[0]:rect[0]+rect[2],rect[1]:rect[1]+rect[3]]
  cv2.imshow('cropped',crop)
  cv2.waitKey(1)
  time.sleep(0.5)
  cv2.destroyAllWindows()
   '''
cv2.imshow("Text detection result", img)
cv2.waitKey()
