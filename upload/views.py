from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
                                     GenericAPIView
                                     )


class UploadFileView(GenericAPIView):

    def __init__(self, **kwargs):
        super(UploadFileView, self).__init__(**kwargs)

    def post(self, request):
        print(request.data)
