from flask import Flask, render_template, request
from werkzeug import secure_filename
import eyed3
import os
app = Flask(__name__)

@app.route('/upload')
def upload():
   return render_template('eye.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join('/home/anitha/Desktop/python/newproj',f.filename ))
      audiofile=eyed3.load(f.filename)
      Artist = request.form['artist']
      ar=unicode(Artist)
      Album = request.form['album']
      al=unicode(Album)
      Title= request.form['title']
      tl=unicode(Title)    
      Image = request.files['image']
      ima=Image.read()      
      audiofile.tag.artist = ar
      audiofile.tag.album = al
      audiofile.tag.title = tl
      audiofile.tag.images.set(3,ima,"image/jpeg",u"front_cover")  
      audiofile.tag.save()
      return "file successfull"


		
if __name__ == '__main__':
   app.run(debug = True)
