import cv2
import numpy as np

#define the order of the points 
def pointOrder(pts):
	#initialize
	rect = np.zeros((4,2),dtype = "float32") #4 points with 2 values of coordinates each
	s = pts.sum(axis = 1) #for all 4 points , sum the values pairs
	rect[0] = pts[np.argmin(s)] # the smallest sum goes as point 0 top-left
	rect[3] = pts[np.argmax(s)] # the largest sum goes as point 4 bottom-right
	diff = np.diff(pts,axis = 1) #for all 4 points , get the difference of each pairs
	rect[1] = pts[np.argmin(diff)] 
	rect[3] = pts[np.argmax(diff)]

	return rect

#warp the target into a rectangular image
def pointTransform(image,pts):
	rect = pointOrder(pts)
	(tl,tr,br,bl) = rect

	#get the width of the target, formula sqrt((x1-x2)^2 + (y1 - y2)^2)
	widthA = np.sqrt((tl[0] - tr[0])**2 + (tl[1] - tr[1])**2)
	widthB = np.sqrt((bl[0] - br[0])**2 + (bl[1] - br[1])**2)
	width = max(int(widthA), int(widthB)) #top and bottom may not be the same especially if distorted, so get the maximum

	#get the height of the target
	heightA = np.sqrt((tl[0] - bl[0])**2 + (tl[1] - bl[1])**2)
	heightB = np.sqrt((tr[0] - br[0])**2 + (tr[1] - br[1])**2)
	height = max(int(heightA), int(heightB))

	#initialize targetImage size
	target = np.array([[0,0],[width-1,0],[width-1,height-1], [0,height - 1]],dtype="float32")

	#compute perspective transform matrix and apply it
	matrix = cv2.getPerspectiveTransform(rect,target)
	warped = cv2.warpPerspective(image, matrix, (width,height))

	return warped