from pytube import YouTube

print('''
        |=======\  |=======\        
        | ------ | |  ----  |
        | |    | | |  |  |  |
        | ------ | |  |  |  |
        |=======/  |  |  |  |  
        |          |  ----  |
        |          |=======/
''')

link = input("   Enter video's link ...\n   ")
print('\n')

try:
    video = YouTube(str(link))
except:
    print('     Something went wrong')
    print('     Check if your link is valid')
    exit('     Exiting app ...')

res = input('   Choose the number of the resolution you like!\n   0: 360\n   1: 720\n   2: 1080\n   ')
options = [ '360p', '720p', '1080p' ]

try:
    chosen_stream = video.streams.filter(file_extension = 'mp4', resolution = options[int(res)])
except:
    print('This resolution is not available')
    exit('Exiting app ...')

print('   Now downloading ', video.title)
download_stream = chosen_stream[0].download('./')
