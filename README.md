# metadata
# add metadata to mp3 file using eyed3 and flask in python
# Here I add some details like artist,album,title and image to the mp3 file.

#flaskeye.py


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




# eye.html

<html>
   
   <body>
   
   <center>      
   
   <table width="600">
   
   <tr><form action = "http://localhost:5000/uploader" method = "POST" enctype = "multipart/form-data"></tr>

<tr><td>File upload </td><td><input type = "file" name = "file" /></td></tr>

<tr><td><p> Artist </td><td><input type = "text" name = "artist" /></p></td></tr>

<tr><td><p>Album </td><td><input type = "text" name = "album" /></p></td></tr>

<tr><td><p>Title </td><td><input type = "text" name = "title" /></p></td></tr>

<tr><td><p>Front_cover</td><td><input type = "file" name = "image" /></td></tr>

<tr><td> </td><td><p><input type = "submit" value = "submit" /></p></td></tr>

</form>

</table>

</center>

</body>

</html>
