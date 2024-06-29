import cv2 as cv
def black(x):
    print(x)
switch="0:OFF \n 1:ON"
cv.namedWindow("image")
cv.createTrackbar("switch","image",0,1,black)
while True:
    img=cv.imread("messi5.jpg")
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
    s=cv.getTrackbarPos("switch","image")
    if s==0:
        pass
    else:
        img=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    cv.imshow("image",img)
cv.destroyAllWindows()