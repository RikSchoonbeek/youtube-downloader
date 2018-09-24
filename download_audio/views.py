from django.conf import settings
from django.shortcuts import render

from .forms import YouTubeVideoURLForm

from .utils import download_youtube_audio


def home(request):
    """
    Display homepage where users can download the audio of a specific
    YouTube video. This will be done with a form in which user's can
    submit a URL for an YouYube video.
    """
    if request.method == "POST":
        form = YouTubeVideoURLForm(request.POST)
        if form.is_valid():
            YouTube_video_url = form.cleaned_data['video_url']
            download_dir = settings.AUDIO_DIR
            download_youtube_audio(YouTube_video_url, download_dir)

            #
    else:
        form = YouTubeVideoURLForm()

    return render(request, 'download_audio/home.html', {'form': form})
