from pytube import YouTube

def startApp():

    link = input('Please enter a link: ')
    yt = YouTube(link)

    print(f'Title: {yt.title}')
    print(f'Length in seconds: {yt.length}')
    print(f'Number of views: {yt.views}')
    print(f'Rating: {yt.rating}')

    # Note you can use Dash streams for higher quality but need audio codec as well
    print(yt.streams.filter(progressive=True))

    ys = yt.streams.get_highest_resolution()

    print('Downloading to current working directory..')
    ys.download()
    ys.print('Download completed!')


startApp()
