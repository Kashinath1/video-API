from rest_framework import viewsets
from .serializers import VideoSerializers
from .models import Video
from moviepy.editor import *
from django.core.exceptions import ValidationError
# Create your views here.

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    # clip = VideoFileClip("video.mp4")
    # clip = clip.subclip(0, 600)
    # duration = clip.duration
    # print("Duration : " + str(duration))
    # clip.ipython_display()
    
    def validate_file_size(value):
        video = value.size
    
        if video > 1024 * 1024 * 1024:
            raise ValidationError("The maximum file size that can be uploaded is 1GB")
        else:
            return value