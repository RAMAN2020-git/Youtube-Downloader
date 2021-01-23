from flask import Flask, render_template, request

from pytube import YouTube

from flask import send_file

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/downloading/', methods=['post', 'get'])
def downloading():
    if request.method == 'POST':
        #return render_template('downloading.html')
        youtube_link = request.form.get('youtube')
        print(youtube_link)
        yt = YouTube(youtube_link)
        stream = yt.streams.first()
        print(stream.default_filename)

        stream.download(filename='video')
    
        return send_file('video.mp4', as_attachment=True, attachment_filename=(stream.default_filename))
        
    
@app.route('/youtube/', methods=['post', 'get'])
def youtube():
    return render_template('youtube.html') 

app.run(host='0.0.0.0')