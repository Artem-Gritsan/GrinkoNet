from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserNet
from .serializers import GetUserNetSerializer, UserNetPublicSerializer, UserNetSerializer
from rest_framework import generics
from rest_framework import permissions, authentication
from rest_framework import status

class ListUsers(generics.ListAPIView):
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer
    # permission_classes = [permissions.IsAdminUser]


class UserNetView(APIView):
    """
    Get  UpDate personal User info
    """
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]
    def get(self, request):
        """
        Return user info
        """
        user = UserNet.objects.get(id=self.request.user.id)
        serializer = UserNetSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = UserNet.objects.get(id=self.request.user.id)
        serializer = UserNetSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserNetPublicView(APIView):
    """
    Get public user info
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            user = UserNet.objects.get(pk=pk)
            serializer = UserNetPublicSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

















# class UserNetView(generics.RetrieveUpdateAPIView):
#     """
#     Get personal user information
#     """
#     queryset = UserNet.objects.all()
#     serializer_class = UserNetSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return UserNet.objects.filter(id=self.request.data)
#
# class UserNetPublicView(generics.ListAPIView):
#     """
#     Get public user information
#     """
#
#     serializer_class = UserNetPublicSerializer
#     permission_classes = [permissions.AllowAny]
#
#     # def get_queryset(self):
#     #     return UserNet.objects.filter(id=self.request.user.id)




