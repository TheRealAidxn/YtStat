import pyfiglet
from pytube import YouTube
import time

render = pyfiglet.figlet_format("YT Stat")
print(render)
time.sleep(3)
#ask for the link from user
url = input("Enter the link of YouTube video you want to check:  ")
yt = YouTube(url)
print("We are now going to check the stats")
#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Number of views in minutes", yt.length / 60, "Minutes")
print("Length of video in seconds: ",yt.length)
print("Rating of video: ",yt.rating)
print("This video was made by ",yt.author)
print("The description of this video is, ", yt.description)
if yt.age_restricted == False:
    print("The video is not age restricted!")
if yt.age_restricted == True:
    print("this video is not age restricted")




