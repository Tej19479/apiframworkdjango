from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from api.models import User,inv,bank_details
from api.serializer import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordVSerializer,SendPasswordRestEmailSerilizer,AddBankDetialsSerializer
UserChangePasswordVSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMessage,send_mail


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }




class UserRegistrationView(APIView):
    renderer_classes =[UserRenderer]
    def post(self, request, format=None):
        serializer =UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           user =serializer.save()
           id = User.objects.filter(email=user).values_list('id',flat=True)
           print("id*****",id)
           for x in id:
             print("8880",x)
             print(type(x))
             inv_state=0
             deleted ='N'
             Inv =inv(uid_id=x,inv_state=inv_state,deleted=deleted)
             Inv.save()
             id1 = inv.objects.filter(uid=x).values()
             print("id1****",id1)
           token =get_tokens_for_user(user)
           
           return Response({'status':'True','Message':'Registration success','status':'200','result':serializer.data,'token':token},status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_404_CREATED)
    
    
    
class UserLoginView(APIView):
    renderer_classes =[UserRenderer]

    def post(self, request, format=None):
        serializer =UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
          email = serializer.data.get('email')
          password =serializer.data.get('password')
          user=authenticate(email=email,password=password)
          if user is not None:
              token =get_tokens_for_user(user)

              return Response({'msg':'Login Success','token':token}, status=status.HTTP_200_OK)
          else:
              return Response({'errors':{'non_field_error':['Email or Password is not Valid']}},
                              status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)



class UserProfileView(APIView):
    renderer_classes =[UserRenderer]
    permission_classes =[IsAuthenticated]
    def get(self,request,format=None):
        serlializer = UserProfileSerializer(request.user)
        return Response(serlializer.data ,status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes =[UserRenderer]
    permission_classes =[IsAuthenticated]
    def post(self,request, format=None):
       
       
        serilizer =UserChangePasswordVSerializer(data=request.data,context={'user':request.user})
        #serilizer =UserChangePasswordVSerializer(password=password['password'], password2=password['password2'])
        #print('serilizer---',serilizer)
        
        if  serilizer.is_valid(raise_exception=True):
            print("serilise=======>",serilizer.data)
            return Response({'msg':'Password Changed succesfully'}, status=status.HTTP_200_OK)                                     
        
        return Response(serilizer.errors,status=status.HTTP_404_BAD_REQUEST)


class SendPasswordRestEmailView(APIView):
    renderer_classess =[UserRenderer]
    def  post(self, request, fromat=None):
        serializer = SendPasswordRestEmailSerilizer(data=request.data)
        if  serializer.is_valid(raise_exception=True):
            return Response({'msg':'Passwordrest link send on email'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)


class UserPasswordRestView(APIView):
    renderer_classess =[UserRenderer]
    def  post(self, request,uid,token, fromat=None):
        serializer = UserChangePasswordVSerializer(data=request.data,context={'token':token,'uid':uid})
        if  serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password change sucessful'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
    
    
class Sendmail(APIView):
    def get(self,request,fromat=None):
        send_mail('Testing Mail',
                  'Here is the message',
                  'golusingh19479@gmail.com',
                 ['tej.pratap@faircent.com'],fail_silently=False, )
        
        return Response({'mg:sussecs'})
    
class AddBankDetials(APIView):
   renderer_classes =[UserRenderer]
   
   def post(self,request,Format=None):
     serializer = AddBankDetialsSerializer(data=request.data)
     print("request data of bank",request.data)
     if  serializer.is_valid(raise_exception=True):
             return Response({'msg':'Add Bank succefully'},status=status.HTTP_200_OK)
     return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

