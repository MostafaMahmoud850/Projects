import pytube
url = input("Enter your URL for download it: ")
pytube.YouTube(url).streams.get_by_resolution().download("desktop")

# pytube.YouTube(url).streams.get_highest_resolution.download("desktop")
# pytube.YouTube(url).streams.get_lowest_resolution.download("desktop")