import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd="C:\\Users\\Tej Pratap\\Desktop\\Rest_framework\\tessaocr\\tesseract.exe"

def image_get_tex(image):    
 
   image =Image.open(image,mode='r')
   #image.show()
   get_text =pytesseract.image_to_string(image)
   return get_text


res =image_get_tex("C:/Users/Tej Pratap/Pictures/20230216_223634.jpg")
print(res)