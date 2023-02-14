from django.core.mail import EmailMessage,send_mail
from django.core import mail
import os
import re
class Util:
    @staticmethod
    def send_email(data):
       email=EmailMessage(
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

    if(str==None):
     return False
    if(re.search(p,str)):
     return True
    else:
     return False
 
  def  isValidIFSCCode(str):
     
        regex = "^[A-Z]{4}0[A-Z0-9]{6}$"
            
        p = re.compile(regex)


        if (str == None):
            return False


        if(re.search(p, str)):
            return True
        else:
            return False
        
        
  def verificationdoc(self):
        pass