from pytubefix import YouTube

#getting link input
link = input("Insert YouTube URL here: ")
yt = YouTube (link)

#destination
destination = "/home/urosh/Videos"

#downloading the video
yt.streams.first().download(output_path=destination)

#result
print(yt.title + " has been successfully downloaded at " + destination)

