from pytube import YouTube


# = input('Enter a youtube video URL: ')
url = "https://www.youtube.com/watch?v=ycPr5-27vSI&t"
print(url)
YT = YouTube(url)
#print(YT.streams.all(),"/")

sizeofFile = YouTube(url).streams.first().filesize
print(sizeofFile)


title = YouTube(url).title
print(title)
#YouTube(url).streams.first().on_progress(chunk="1024", file_handler=title, bytes_remaining=sizeofFile)

AmountofChunks = sizeofFile / 1024
print(AmountofChunks)

YouTube(url).streams.first().download()


#YouTube(url).streams.first().download()



#def on_progress(stream, chunk, file_handle, bytes_remaining):

#progress_function()





