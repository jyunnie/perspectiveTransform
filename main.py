from transform import pointTransform
import numpy as np 
import cv2

filename = "./resultImg.jpg"
img_url = "./sourceImg1.jpg"
image = cv2.imread(img_url)

#coords = [(449.75, 466.25),(763.25, 775.25),(670.25, 1114.25),(656.75, 1129.25)] #y,x
coords = [(667.25, 449.7),(1118.7, 464.7),(653.8, 761.7),(1126.2, 784.25)] #x,y
pts = np.array(coords,dtype = "float32")

warped = pointTransform(image, pts)
cv2.imshow("title",warped)
cv2.imwrite(filename, warped)
cv2.waitKey(0)
