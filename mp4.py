from pytubefix import YouTube

#getting link input
link = input("Insert YouTube URL here: ")
yt = YouTube (link)

#destination
destination = "/path/of/your/own/choice" #choose where do you want to download the video

#downloading the video
yt.streams.first().download(output_path=destination)

#result
print(yt.title + " has been successfully downloaded at " + destination)

