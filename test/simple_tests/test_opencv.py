import numpy as np
import sys
#import cv2




if False:
    import Lamia.Lamia.libs.opencv27.cv2 as cv2
else:
    #sys.path.append("U://FR//BOR//VT//PVR//20_LAMIA//0_Github//Lamia//Lamia//libs//opencv37")
    import Lamia.Lamia.libs.opencv37.cv2 as cv2
    #import cv2

cam = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cam.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()

print('ok')