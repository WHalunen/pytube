#length is working fine

from pytube import YouTube
import math

#ENTER A YOUTUBE VIDEO 'URL
url = 'https://www.youtube.com/watch?v=kHLHSlExFis'
yt = YouTube(url)
print('video description: ', yt.description)
#print('rating', yt.rating)
length=yt.length



#print('views', yt.views)
length_int=int(length)
length_min=math.floor(length_int / 60)
length_seconds=length_int % 60
print(length_min,"minute(S)",length_seconds,"Second(S)")
