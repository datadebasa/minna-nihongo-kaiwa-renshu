from flask import Flask
from flask import render_template
import os
from flask import send_from_directory, abort

class Config:
    def gemini_core(self):
        return 'gemini_core'
    
    
gemini = Config()
print(gemini.gemini_core())
app = Flask(__name__)

AUDIO_FOLDER = os.path.join('static', 'assets', '0-0001-01-230001')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/v1/message')
def hello():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return 'About'
@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/audios')
def list_audios():
    """Menampilkan semua file dan folder"""
    if not os.path.isdir(AUDIO_FOLDER):
        files = []
    else:
        files = os.listdir(AUDIO_FOLDER)
    return render_template('audio_list.html', files=files)

@app.route('/audios/play/<filename>')
def play_audio(filename):
    print(f"Memutar audio: {filename}")
    """Menampilkan pemutar audio jika file ditemukan"""
    if not os.path.isfile(os.path.join(AUDIO_FOLDER, filename)):
        abort(404, description="File tidak ditemukan")
    return render_template('audio_player.html', filename=filename)

@app.route('/audios/files/<filename>')
def serve_audio(filename):
    """Melayani file mp3 langsung"""
    file_path = os.path.join(AUDIO_FOLDER, filename)
    print(f"Melayani file audio: {filename} status {os.path.isfile(file_path)}")
    if not os.path.isfile(file_path):
        print(f"File tidak ditemukan: {filename}")
        return render_template('audio_not_found.html', filename=filename)
    return send_from_directory(AUDIO_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)