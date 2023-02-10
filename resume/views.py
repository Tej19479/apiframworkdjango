from django.shortcuts import render
from rest_framework.response import Response
from resume.models import Profile
from rest_framework.views import APIView
from rest_framework import status
from resume.serializer import ProfileSerializer

class ProfileView(APIView):
    
    def post(self ,request , format=None):
        serilizer = ProfileSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Resume Uploaded Successfully','status':'sucess','candidate':serilizer.data},status=status.HTTP_201_CREATED)
        
        return Response(serilizer.errors)
    
    
    
    def get(self ,request , format=None):
        candiate =Profile.objects.all()
        serializer =ProfileSerializer(candiate,many=True)
        return Response({'status':'success','candidates':serializer.data},status=status.HTTP_200_OK)