from pytube import YouTube

link = input("Enter the link of the video: ")

yt = YouTube(link)
yt.streams.get_highest_resolution().download("./Videos")
print("Done!")