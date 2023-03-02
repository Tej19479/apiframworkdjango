import cv2

#Break Video into Mutiple Images and store in a floder

Vidcap =cv2.VideoCapture(r"C:\Users\Tej Pratap\Downloads\https___qc6.faircent.com_lender_registration_v2_step3.mp4")
ret ,img =Vidcap.read()#Read The vedio
count =0
while True:
    if ret==True:
        cv2.imwrite("D:\\Frame\\imageN%d.jpg"%count,img)
        Vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret ,img=Vidcap.read()
        cv2.imshow("res",img)
        print(count)
        count +=1
        
        if cv2.waitKey(1) & 0xFF ==ord("q"):
            break
            cv2.destroyAllWindows()
Vidcap.release()
cv2.destroyAllWindows()