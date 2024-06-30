import cv2 as cv
import numpy as np
img=cv.imread("messi5.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img1=cv.imread("template.png",0)
w,h=img1.shape[::-1]
result=cv.matchTemplate(gray,img1,cv.TM_CCOEFF_NORMED)
print(result)
threshold=0.467
loc=np.where(result >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)
cv.imshow("template",img1)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()