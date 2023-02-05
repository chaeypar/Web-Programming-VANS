from .models import User, AuthToken
from .serializer import UserSerializer

from rest_framework import generics, status
from rest_framework.response import Response


class UserSignUp(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        if User.objects.filter(email=request.data['email']).exists():
            return Response(data={"status": "FAILED", "message": "이미 존재하는 이름입니다."},
                            status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(nickname=request.data['nickname']).exists():
            return Response(data={"status": "FAILED", "message": "이미 존재하는 닉네임입니다."},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        token = AuthToken.objects.create(user=user)
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'id': str(user.id), 'token': str(token.id)}, status=status.HTTP_201_CREATED)
    
class UserLogin(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email) # stip().lower()?
        except User.DoesNotExist:
            return Response({'error':'존재하지 않는 유저입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if user.check_password(password):
            token = AuthToken.objects.create(user=user)
            serializer = self.get_serializer(data=user)
            serializer.is_valid(raise_exception=True)
            return Response({'token': str(token.id), 'info': serializer.data}, status=status.HTTP_200_OK)
        else:
        	return Response({'error':'비밀번호가 맞지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        

  
        
  
        
        

