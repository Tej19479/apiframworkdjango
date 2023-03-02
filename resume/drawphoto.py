import cv2 as cv
import numpy as np

#img1 = cv.imread("C:/Users/Tej Pratap/Pictures/20230216_223634.jpg",1)
#img1=cv.resize(img1,(500,500))
#cv.line(img1,(0,125),(255,255),(255,0,125),8)
#cv.arrowedLine(img1,(0,125),(255,255),(255,0,125),8)
#cv.rectangle(img1,(25,25),(255,255),(255,0,125),-1)
#font=cv.FONT_HERSHEY_COMPLEX_SMALL
#img1=np.ones([512,512,3],np.uint8)*255 black
img1=np.zeros([512,512,3],np.uint8)*255 #white image
color = (255)

cv.circle(img1,(220,125),65,(255,0,125),8)
cv.ellipse(img1,(25,60),(0,270),0,0,270,color,5)
#text
#img1 =cv.putText(img1,"THOR",1,(20,50),font,2,(0,125,255),10,cv.LINE_AA)

 #Line thickness of 2 px
thickness = 2
color = (255, 0, 0)
fontScale = 1  
org = (50, 50)
font = cv.FONT_HERSHEY_SIMPLEX
# Using cv2.putText() method#esciplce method ecslipe
img1 = cv.putText(img1, 'Pancard', org, font,  fontScale, color, thickness, cv.LINE_AA)

cv.imshow("original",img1)
cv.waitKey()
cv.destroyAllWindows()