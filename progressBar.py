from pytube import YouTube
import math


#PROMPT USER FOR INPUT
print('\nNOTICE: THIS IS ONLY FOR YOUTUBE VIDEOS')
url = input('Enter a youtube video URL (FORMAT: "URL"): ')

YT = YouTube(url)
title = YT.title

print("\nTITLE: ", title)

#LENGTH OF VIDEO CONVERSION FROM SECONDS -> TO MINUTES AND SECONDS
length = YT.length
length_int = int(length)
length_mins = math.floor(length_int / 60)
length_seconds = length_int % 60
print("Length: ", length_mins, " Minutes and ", length_seconds, " Seconds")

#SIZE OF VIDEO CONVERSION FROM BYTES -> MB
sizeofFile = YT.streams.first().filesize
AmountOfChunks = sizeofFile / 1000000
print("FILE SIZE: ", round(AmountOfChunks), "MB")

#DISPLAY VIDEO URL
print("LINK: ", url)

YT.streams.first().download()


