from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import User
from .serializers import UserSerializer, MiniUserSerializer
from django.contrib.auth import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class UserView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serialized = UserSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.validated_data
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     name = request.POST.get('name')
    #     mobile = request.POST.get('mobile')
        
    #     check_user = User.objects.filter(email = email).first()
    #     check_profile = Profile.objects.filter(mobile = mobile).first()
        
    #     if check_user or check_profile:
    #         context = {'message' : 'User already exists' , 'class' : 'danger' }
    #         return render(request,'register.html' , context)
            
    #     user = User(email = email , first_name = name)
    #     user.save()
    #     otp = str(random.randint(1000 , 9999))
    #     profile = Profile(user = user , mobile=mobile , otp = otp) 
    #     profile.save()
    #     send_otp(mobile, otp)
    #     request.session['mobile'] = mobile
    #     return redirect('otp')
    # return render(request,'register.html')
    