from pytube import YouTube


url = input('Enter a youtube video URL: ')
print(url)
YT = YouTube(url)
#print(YT.streams.all(),"/")


#YouTube.streams.all()
YouTube(url).streams.first().download()

