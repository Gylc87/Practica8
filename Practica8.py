import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplaciano = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    border = cv2.blur(frame, (5,5))
    bordes = cv2.Canny(border, 30, 100)

    cv2.imshow("Original", frame)
    cv2.imshow("laplaciano", laplaciano)
    cv2.imshow("sobely", sobely)
    cv2.imshow("sobelx", sobelx)
    cv2.imshow("canny", bordes)
    

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()