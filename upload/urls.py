from django.conf.urls import url
from .views import (UploadFileView
                    )


urlpatterns = [
    url('uploadfile', UploadFileView.as_view(), name='upload-file'),
]