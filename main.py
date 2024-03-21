import cv2
import numpy as np
red = cv2.imread("RED.tif")[:,:,2]/255
green = cv2.imread("GREEN.tif")[:,:,1]/255
out = np.logical_and(red>.2 ,green>.4)
cv2.imwrite('out.png',out*255)