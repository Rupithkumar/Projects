import cv2 as cv
import numpy as np
def color(x):
    print(x)
cap=cv.VideoCapture(0)
cv.namedWindow("tracking")
cv.createTrackbar("LH","tracking",0,255,color)
cv.createTrackbar("LS","tracking",0,255,color)
cv.createTrackbar("LV","tracking",0,255,color)
cv.createTrackbar("UH","tracking",255,255,color)
cv.createTrackbar("US","tracking",255,255,color)
cv.createTrackbar("UV","tracking",255,255,color)
while True:
    _,frame=cap.read()
    hsv=cv.cvtColor(frame,cv.COLOR_RGB2HSV)
    l_h=cv.getTrackbarPos("LH","tracking")
    l_s=cv.getTrackbarPos("LS","tracking")
    l_v=cv.getTrackbarPos("LV","tracking")
    u_h=cv.getTrackbarPos("UH","tracking")
    u_s=cv.getTrackbarPos("US","tracking")
    u_v=cv.getTrackbarPos("UV","tracking")
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow("image",frame)
    cv.imshow("mask", mask)
    cv.imshow("result", res)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()