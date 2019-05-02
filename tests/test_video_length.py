#length is working fine

from pytube import YouTube
#ENTER A YOUTUBE VIDEO 'URL
url = 'https://www.youtube.com/watch?v=kHLHSlExFis'
yt = YouTube(url)
print('video description: ', yt.description)
#print('rating', yt.rating)
print('length', yt.length)
#print('views', yt.views)