from pytube import YouTube

def ytDownload(link,path):
    #Youtube obj
    yt = YouTube(link)  
    try: 
        #downloading the video 
        yt.streams.first().download(path) 
    except: 
        print("Exception caught") 


s = input("YouTube Video URL: ")
p = input("Folder Path: ")
#raw path
path = r'%s'%p
#print(path)
ytDownload(s,path)
