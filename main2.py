from flask import Flask, render_template, request

from gpiozero import LED

from pytube import YouTube

from flask import send_file

from pymkv import MKVFile, MKVTrack

led = LED(17)

app=Flask(__name__)

led.off()
def done_download(test, file):
    led.off()


@app.route('/')
def home():
    return 'Home'

@app.route('/downloading/', methods=['post', 'get'])
def downloading():
    if request.method == 'POST':
        return render_template('downloading.html')
        youtube_link = request.form.get('youtube')
        subtitle = request.form.get('subtitles')
        print(youtube_link)
        yt = YouTube(youtube_link, on_complete_callback=done_download)
        stream = yt.streams.first()
        print(stream.default_filename)
        led.on()
        print(yt.captions.all())
        
        if (subtitle) :
            caption = yt.captions.get_by_language_code('a.en')
            if (caption.download):
                caption.download('subtitle')
            
        stream.download(filename='video')
        
        mkv = MKVFile()
        mkv.add_track('video.mp4')
        
        if (subtitle):
            mkv.add_track('subtitle (a.en).srt')
            
        mkv.mux('output.mkv')
        
        
    
@app.route('/youtube/', methods=['post', 'get'])
def youtube():
    return render_template('youtube.html') 
    

        

@app.route('/return-files/')
def return_files_tut():
    try:
        return send_file('test.txt', as_attachment=True)
    except Exception as e:
        return str(e) 

@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    
    
    if request.method == 'POST':
        youtube = request.form.get('youtube')  # access the data inside 
        password = request.form.get('password')
        youtube_link = request.form.get('youtube')

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
            led.on()
        else:
            message = "Wrong username or password"
            led.off()

    return render_template('login.html', message=message)

app.run(host='0.0.0.0')