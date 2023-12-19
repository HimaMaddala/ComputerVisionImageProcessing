import numpy as np
import cv2

img = cv2.imread("D:\\B21AI002_CVIP\\img3.jpg")

row,col,_=img.shape

pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
M=cv2.getAffineTransform(pts1, pts2)

dst=cv2.warpAffine(img,M,(col,row))
cv2.imshow("Affine Transformation", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
