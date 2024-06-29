import numpy as np
import cv2 as cv


def color(x):
    print(x)


img = np.zeros((900, 900, 3), np.uint8)
cv.namedWindow("image")
switch = '0:OFF \n 1:ON'
cv.createTrackbar("B", "image", 0, 255, color)
cv.createTrackbar("G", "image", 0, 255, color)
cv.createTrackbar('R', "image", 0, 255, color)
cv.createTrackbar("switch", "image", 0, 1, color)
while True:
    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    b = cv.getTrackbarPos("B", "image")
    g = cv.getTrackbarPos("G", "image")
    r = cv.getTrackbarPos("R", "image")
    s = cv.getTrackbarPos("switch", "image")
    if s == 0:
        pass
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()
