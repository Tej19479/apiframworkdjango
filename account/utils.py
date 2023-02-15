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


class imageconvert:
  pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Tej Pratap\\Desktop\\Rest_framework\\tessaocr\\tesseract.exe"
  def image_get_tex(image):
    image = Image.open(image, mode='r')
    # image.show()
    get_text = pytesseract.image_to_string(image)
    return get_text
  
  def imgaetobase64(image):
       with open(image, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
        return   converted_string.decode('utf-8')
