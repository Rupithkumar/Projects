import cv2 as cv
import numpy as np
def color(x):
    print(x)
cv.namedWindow("tracking")
cv.createTrackbar("LH","tracking",0,255,color)
cv.createTrackbar("LS","tracking",0,255,color)
cv.createTrackbar("LV","tracking",0,255,color)
cv.createTrackbar("UH","tracking",255,255,color)
cv.createTrackbar("US","tracking",255,255,color)
cv.createTrackbar("UV","tracking",255,255,color)
while True:
    img=cv.imread("messi5.jpg")
    hsv=cv.cvtColor(img,cv.COLOR_RGB2HSV)
    l_h=cv.getTrackbarPos("LH","tracking")
    l_s=cv.getTrackbarPos("LS","tracking")
    l_v=cv.getTrackbarPos("LV","tracking")
    u_h=cv.getTrackbarPos("UH","tracking")
    u_s=cv.getTrackbarPos("US","tracking")
    u_v=cv.getTrackbarPos("UV","tracking")
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(img,img,mask=mask)
    cv.imshow("image",img)
    cv.imshow("mask", mask)
    cv.imshow("result", res)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cv.destroyAllWindows()