from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

"""
Purpose: This api uses create to cerate the new user.
@params: (viewsets.ModelViewSet) viewset provide get data by default.
@return: message
"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    # create new user with encrypted password.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message":"User created Successfuly"}, status=status.HTTP_200_OK, headers=headers)


"""
Purpose: This api add POST data to the database
@params: ((generics.ListCreateAPIView) Provide list of data.
@return: message
"""
class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # Get all the records from post table.
    def get(self , request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    # Add new record in the post table.
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid()
        serializer.save(author=request.user)
        return Response({"message":"Data added Successfuly"}, status=status.HTTP_200_OK)