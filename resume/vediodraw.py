import cv2
from cv2 import VideoCapture
import datetime


#pip install ffmpeg-python
cap = cv2.VideoCapture(r"C:\Users\Tej Pratap\Downloads\https___qc9.faircent.com_lender_registration_step1.mp4")
print("cap",cap)
print("width==",cap.get(3))
print("hieht==",cap.get(4))

while True:
    ret ,frame =cap.read()
    frame =cv2.resize(frame,(500,450))
    font = cv2.FONT_HERSHEY_SIMPLEX
    date_date="Date:"+str(datetime.datetime.now())
    text='Height:'+str(cap.get(4))+'width:'+str(cap.get(3))
    frame = cv2.putText(frame, text, (10,250), font,1,(0,155,255), 1, cv2.LINE_AA)
    frame = cv2.putText(frame, date_date, (10,50), font,1,(0,155,255), 1, cv2.LINE_AA)

   # gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    k= cv2.waitKey(30)
    if (k==ord("q")):
        break
    
    
cap.release()
cv2.destroyAllWindows()
     