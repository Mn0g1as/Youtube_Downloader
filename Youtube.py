from pytube import Youtube

# Paste your Youtube link :)
link = "https://youtu.be/paste-your-youtube-link"
yt = Youtube(link)
stream = yt.streams.get_highest_resolution

print("Downloading. Please wait...")
stream.download()
print("Download completed.")

