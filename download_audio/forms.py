from django import forms


class YouTubeVideoURLForm(forms.Form):
    video_url = forms.URLField(label='Enter YouTube video URL')