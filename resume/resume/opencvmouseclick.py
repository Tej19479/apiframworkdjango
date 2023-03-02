import cv2
import numpy as np
'''
def draw(event, x, y,flags,param):
     if event==cv2.EVENT_LBUTTONDBLCLK:
         cv2.circle(img,(x,y),100,(125,0,255),5)
     if event==cv2.EVENT_RBUTTONDBLCLK:
         cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
         
         
cv2.namedWindow(winname="res")

img=np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("res",draw)
while True:
 cv2.imshow("res",img)
 if cv2.waitKey(1)& 0xFF==27: 
    break
cv2.destroyAllWindows()'''


#create a function which help to find cordinate of any pixel and its color

def mouse_event(event,x,y,flage,param):
    print("event===",event)
    print("x===",x)
    print("y===",y)
    print("flage==",flage)
    print("params==",param)
    font =cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,', ',y)
        
        cord =". "+str(x)+', '+str(y)
        cv2.putText(img,cord,(x,y),font ,1,(155,125,100),2)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]#for blue channel is 0
        g =img[y,x,1]#for green channel is 1
        r =img[y , x,2] # for red channel is 2
        color_bgr=". "+str(b)+', '+str(g)+', '+str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(152,255,130),2)
        #cv2.imshow('image',img)
cv2.namedWindow(winname="res")
img=np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("res",mouse_event)
while True:
 cv2.imshow("res",img)
 if cv2.waitKey(1)& 0xFF==27: 
    break
cv2.destroyAllWindows()  
    
        
        