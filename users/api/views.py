from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from . import serializers
from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/update_user.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response({'serializer': serializer, 'user': user})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(User, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'user': user})
        serializer.save()
        return redirect('users/user-list')
