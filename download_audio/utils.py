import uuid

from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable


def download_youtube_audio(url, download_dir):
    """
    This function takes a youtube video url and download location (directory),
    downloads an audio stream for the video at that URL to the given download
    location.
    """
    yt = get_yt_object(url)
    stream = get_best_quality_audio_stream(yt)
    unique_filename = create_unique_file_name()
    stream.download(output_path=download_dir,
                    filename=unique_filename)


def get_yt_object(url):
    """
    Takes a URL and tries to get an pytube yt instance (see pytube docs).
    """
    try:
        return YouTube(url)
    except RegexMatchError:
        # Notify user that they need to enter a valid YouTube URL
        return {"error": "Please enter a valid YouTube URL."}
    except VideoUnavailable:
        # Notify user that an video could not be found using that URL
        return {"error": "A video could not be found using that URL."}
    except:
        # Notify user that something went wrong, but that we don't know what exactly
        return {"error": "Something went wrong, but we're not exactly sure what. Our team has been notifid of this error and will try to solve it as soon as possible."}


def get_best_quality_audio_stream(yt_object):
    """
    Takes an yt object, returns the audio stream with the highest available quality.
    """
    return yt_object.streams.filter(only_audio=True).order_by('abr').desc().first()


def create_unique_file_name():
    """
    This function creates a unique filename
    """
    filename = str(uuid.uuid4().hex)
    return filename


def save_audio_file_to_database(file):
    """
    Takes a downloaded audio file and saves it to the database.
    """