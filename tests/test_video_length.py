#length is working fine

from pytube import YouTube         # LET 'S  START BY IMPORTING THE YOUTUBE CLASS
import math

#ENTER A YOUTUBE VIDEO 'URL
url = 'https://www.youtube.com/watch?v=kHLHSlExFis'
yt = YouTube(url)  # HERE WE HAVE A YOUTUBE OBJECT THAT WE NAMED YT
print('video description: ', yt.description)
length=yt.length

length_int=int(length)
length_min=math.floor(length_int / 60)
length_seconds=length_int % 60
print(length_min,"minute(S)",length_seconds,"Second(S)")
