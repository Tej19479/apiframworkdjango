import cv2
from cv2 import VideoCapture


'''
only per webcame open
#pip install ffmpeg-python
cap = cv2.VideoCapture(0)
print("cap",cap)

while cap.isOpened():
    ret ,frame =cap.read()
    if ret ==True:
     frame =cv2.resize(frame,(500,700))
     gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     cv2.imshow("frame",frame)
     cv2.imshow("gray",gray)
     k= cv2.waitKey(1)
     if k ==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()'''
     
#only per webcame open and save
cap = cv2.VideoCapture(0)
print("cap",cap)
fourcc =cv2.VideoWriter_fourcc(*"XVID")

output =cv2.VideoWriter("D:\\save.avi",fourcc,20.0,(640,480))

while cap.isOpened():
    ret ,frame =cap.read()
    if ret ==True:
     #frame =cv2.resize(frame,(500,700))
     gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     cv2.imshow("frame",frame)
     #cv2.imshow("gray",gray)
     output.write(frame)
     k= cv2.waitKey(1)
     if k ==ord('q'):
        break
    
    
cap.release()
output.release()
cv2.destroyAllWindows()