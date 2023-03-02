import cv2
 
 #grayscale
'''img1 = cv2.imread("C:/Users/Tej Pratap/Pictures/20230216_223634.jpg",0)
img1=cv2.resize(img1,(500,500))
print(img1)
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()
#orgialn image
img1 = cv2.imread("C:/Users/Tej Pratap/Pictures/20230216_223634.jpg",1)
img1=cv2.resize(img1,(500,500))
print(img1)
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()
High stausted
img1 = cv2.imread("C:/Users/Tej Pratap/Pictures/20230216_223634.jpg",-1)
img1=cv2.resize(img1,(500,500))
print(img1)
cv2.imshow("Unchanged",img1)
cv2.waitKey()C:\Users\Tej Pratap\Pictures\Camera Roll\WIN_20220314_16_08_47_Pro.jpg
cv2.destroyAllWindows()
'''


#usere enter path save to another directory
path =input(r"C:/Users/Tej Pratap/Pictures/20230216_223634.jpg")

print("your enter path is ",path)

#Now read a image is 
img1 =cv2.imread(path,0)#convet a grayscale image into 
img1 = cv2.resize(img1,(500,700))

k =cv2.waitkey(0)
if k==ord("s"):
    cv2.imwrite("D:\\output.png",img1)
else:
    cv2.destroyAllWindows()
    
    
    #
    path =input(r"C:/Users/Tej Pratap/Pictures/20230216_223634.jpg")

print("your enter path is ",path)

#Now read a image is 
img1 =cv2.imread(path,0)#convet a grayscale image into 
img1 = cv2.resize(img1,(500,700))
img1 =cv2.flip(img1,1)
k =cv2.waitkey(0)
if k==ord("s"):
    cv2.imwrite("D:\\output.png",img1)
else:
    cv2.destroyAllWindows()
