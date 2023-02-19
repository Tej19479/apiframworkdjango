from django.core.mail import EmailMessage, send_mail
from django.core import mail
import os
import re
import pytesseract
from PIL import Image
import base64


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )
        email.send()


class regex:

    def isaccountvaildation(str):
        regex = "^[0-9]{9,18}$"

        p = re.compile(regex)

        if (str == None):
            return False
        if (re.search(p, str)):
            return True
        else:
            return False

    def isValidIFSCCode(str):

        regex = "^[A-Z]{4}0[A-Z0-9]{6}$"

        p = re.compile(regex)

        if (str == None):
            return False

        if (re.search(p, str)):
            return True
        else:
            return False

    def verificationdoc(panCardNo, adhaar):
        regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
        regex1 = ("^[2-9]{1}[0-9]{3}\\" +
                  "s[0-9]{4}\\s[0-9]{4}$")

        p = re.compile(regex)
        p1 = re.compile(regex1)
        result = ''
        for i in range(0, len(adhaar), 4):
            if i > 0:
                result += ' '
            result += adhaar[i:i+4]
        if (panCardNo == None) and (adhaar == None):
            return False

        if (re.search(p, panCardNo) and len(panCardNo) == 10) and (re.search(p1, result)):
            return True
        else:
            return False

    def pan_read_data(text):
        name = None
        fname = None
        dob = None
        pan = None
        nameline = []
        dobline = []
        panline = []
        text0 = []
        text1 = []
        text2 = []
        lines = text.split('\n')
        for lin in lines:
              s = lin.strip()
              s = lin.replace('\n', '')
              s = s.rstrip()
              s = s.lstrip()
              text1.append(s)
        text1 = list(filter(None, text1))
        print("text1 fliter****************************\n",text1) 
        print("**********************************")          
        lineno = 0
        for wordline in text1:
                xx = wordline.split('\n')
                print("text1 fliter****************************\n",xx) 
                print("*********************************")
                if ([w for w in xx if re.search('(INCOMETAXDEPARWENT|INCOME|TAX|GOW|GOVT|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA)$', w)]):
                 text1 = list(text1)
                print("textIncomatext****************************\n",text1) 
                print("***************************************")

                lineno = text1.index(wordline)
                break
        text0 = text1[lineno+1:]
        print("texto****************\n",text0)
        print("*********************************")
        try:  
        # Cleaning first names
                name = text0[0]
                print("name*********************\n",name)
                print("****************************")
                print(name)
                name = name.rstrip()
                name = name.lstrip()
                name = name.replace("8", "B")
                name = name.replace("0", "D")
                name = name.replace("6", "G")
                name = name.replace("1", "I")
                
            # Cleaning Father's name
                fname = findword(text1,"Father")
                
                #fname = text0[1]
                #fname = fname.rstrip()
                print("fname****dddddd***********\n",fname) 
                print("****5555555555555555555555555***************")
               # fname = fname.lstrip()
                fname = fname.replace("8", "S")
                fname = fname.replace("0", "O")
                fname = fname.replace("6", "G")
                fname = fname.replace("1", "I")
                fname = fname.replace("\"", "A")
                fname = re.sub('[^a-zA-Z] +', ' ', fname)
           
                print("fname***************\n",fname) 

            # Cleaning PAN Card details
                text0 = findword(text1, '(Pormanam|Number|umber|Account|ccount|count|Permanent|ermanent|manent|wumm)$')
                print("Cleaning PAN Card detail\n",text0)
                print("*************************************")
                panline = text0[0]
                pan = panline.rstrip()
                pan = pan.lstrip()
                pan = pan.replace(" ", "")
                pan = pan.replace("\"", "")
                pan = pan.replace(";", "")
                pan = pan.replace("%", "L")
                print("pan********************\n",pan)
                print("****************************")
        except:
            pass 
        
        data = {}
        data['Name'] = name
        data['Father Name'] = fname
        data['Date of Birth'] = dob
        data['PAN'] = pan
        data['ID Type'] = "PAN"
        print("data",data)
        return data
            
def findword(textlist, wordstring):
        lineno = -1
        for wordline in textlist:
            xx = wordline.split()
            if ([w for w in xx if re.search(wordstring, w)]):
                lineno = textlist.index(wordline)
                textlist = textlist[lineno+1:]
                return textlist
        return textlist
    


class imageconvert:
    pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Tej Pratap\\Desktop\\Rest_framework\\tessaocr\\tesseract.exe"

    def image_get_tex(image):
        image = Image.open(image, mode='r')
       # image.show()
        get_text = pytesseract.image_to_string(image)
        img = image.convert('RGB')
        pix = img.load()
        print("image",img) 
        print("pixel\n",pix)
        for y in range(img.size[1]):
             
    	    for x in range(img.size[0]):
		        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
			         pix[x, y] = (0, 0, 0, 255)
		        else:
			        pix[x, y] = (255, 255, 255, 255)
        img.save('temp.jpg')
        return get_text

    def imgaetobase64(image):
        with open(image, "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
            return converted_string.decode('utf-8')
        

