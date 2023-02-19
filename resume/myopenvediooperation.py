import cv2
from cv2 import VideoCapture



#pip install ffmpeg-python
cap = cv2.VideoCapture(r"C:\Users\Tej Pratap\Downloads\https___qc6.faircent.com_lender_registration_v2_step3.mp4")
print("cap",cap)

while True:
    ret ,frame =cap.read()
    frame =cv2.resize(frame,(500,700))
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k= cv2.waitKey(25)
    if (k=="q"):
        break
    
    
cap.release()
cv2.destroyAllWindows()
     