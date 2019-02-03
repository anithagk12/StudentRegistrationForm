from __future__ import unicode_literals
from flask import Flask, render_template, request
from werkzeug import secure_filename
import eyed3
import os
import youtube_dl
app = Flask(__name__)

@app.route('/upload')
def upload():
   return render_template('youtube.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        url1=request.form['url']
        #return(url1)	
        

    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl':'%(title)s-%(id)s.%(ext)s'
}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url1, download=True)
        mp3FileName = ydl.prepare_filename(info).replace(info['ext'], 'mp3')
    print(mp3FileName)
    newfile=mp3FileName.split(" ",1)[0]
    identify=newfile + "mp3file"
    newFileName=newfile + ".mp3"
    os.rename(mp3FileName,newFileName)
    audiofile=eyed3.load(newFileName)
    Title= request.form['title']
    if not (Title==""):
        Title=Title
    else:
        Title="kanniyam"     
    Artist = request.form['artist']
    if not (Artist==""):
        Artist=Artist
    else:    
        Artist="Kanniyam"
    Album = request.form['album']
    if not (Album==""):
        Album=Album
    else:    
        Album="Kanniyam"
    Genre = request.form['genre']
    if not (Genre==""):
        Genre=Genre
    else:    
        Genre="Podcast"
    Source_url = bytes(request.form['source_url'],'utf-8')
    if not (Source_url==""):
        Source_url=Source_url
    else:    
        Source_url=""    
    License = str(request.form['license'])
    if not (License==""):
        License=License
    else:    
        License="https://creativecommons.org/licenses/by/4.0/"
    Comments = str(request.form['comments'])
    if not (Comments==""):
        Comments=Comments
    else:    
        Comments=""
    Language = str(request.form['language'])
    if not (Language==""):
        Language=Language
    else:    
        Language="Tamil"
    Art_name = request.form['art_name']
    if not (Art_name==""):
        Art_name=Art_name
    else:    
        Art_name="Kanniyam"
    Publisher_url = bytes(request.form['publisher_url'],'utf-8')
    if not (Publisher_url==""):
        Publisher_url=Publisher_url
    else:    
        Publisher_url="http://www.kaniyam.com"
    print (type(Publisher_url))
    print ("ssss")    
    audiofile.tag.title = u""+Title    
    audiofile.tag.artist = u""+Artist
    audiofile.tag.album = u""+Album
    audiofile.tag.genre = u""+Genre
    audiofile.tag.source_url = b""+Source_url
    audiofile.tag.license = u""+License
    audiofile.tag.comments.set(u""+Comments, description=u"")
    audiofile.tag.language = u""+Language
    audiofile.tag.art_name = u""+Art_name
    audiofile.tag.publisher_url = b""+Publisher_url
    
    print ("before save")  
      
    audiofile.tag.save()
    print ("file upload to archive.org")
    ia_upload = "ia upload " + identify + \
" -m collection:opensource -m mediatype:audio -m sponsor:Kaniyam -m language:ta " + \
newFileName
    os.system(ia_upload)
    print ("file uploaded")
    return "File updated"


		
if __name__ == '__main__':
   app.run(debug = True)
