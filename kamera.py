import os
import cv2


kam=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
ckt=cv2.VideoWriter('kamra.avi',fourcc,20.0,(640,480))



while True:
    ret,grnt=kam.read()
    grnt=cv2.rectangle(grnt,(250,400),(400,250),(0,255,0),4)
    ckt.write(grnt)
    cv2.imshow("hasangörüntü",grnt)

    if cv2.waitKey(30)& 0xFF==ord('q'):
        break

kam.release()
ckt.release()
cv2.destroyAllWindows()
