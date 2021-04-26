from django.shortcuts import render
from pytube import YouTube
from pytube import Playlist

def index(request):
    return render(request, 'index.html')

def video_download(request):
    
    url = request.GET.get('ytlink')
    yt_video = YouTube(url)
    yt_streams = yt_video.streams.filter(progressive=True, mime_type='video/mp4').order_by('resolution')
    yt_audio = yt_video.streams.filter(only_audio=True)

    embedlink = url.replace("watch?v=", "embed/")

    # if request.method == "POST":
    #     for stream in yt_streams:
    #         video = yt_video.streams.get_by_itag(stream.itag)
    #     video.download()

    context = {
        'yt_video': yt_video,
        'yt_streams': yt_streams,
        'yt_audio': yt_audio,
        'embedlink': embedlink,
    }

    return render(request, 'video.html', context=context)

def playlist_download(request):
    if request.method == "POST":
        url = request.POST.get('ytplaylink')
        ytlist = Playlist(url)

        context = {
            'ytlist': ytlist,
        }
        return render(request, 'playlist.html', context=context)

    return render(request, 'playlist.html')