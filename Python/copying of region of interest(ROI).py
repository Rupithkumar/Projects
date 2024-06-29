import cv2 as cv
img=cv.imread('messi5.jpg')
print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv.split(img)
img=cv.merge((b,g,r))
ball=img[280:340,330:390]
img[273:333,100:160]=ball
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()