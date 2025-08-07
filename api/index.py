from flask import Flask
from flask import render_template
import os, requests
from flask import send_from_directory, abort, request, jsonify

class Config:
    def gemini_core(self):
        return 'gemini_core'
    
    
gemini = Config()
print(gemini.gemini_core())
app = Flask(__name__)

AUDIO_FOLDER = os.path.abspath(os.path.join('api', 'static', 'assets', '0-0001-01-230001'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/v1/message')
def hello():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return render_template('about.html')
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
    return send_from_directory(AUDIO_FOLDER, filename, as_attachment=False)


@app.route('/api/v1/kaiwa', methods=['POST'])
def kaiwa_proxy():
    """
    Proxy endpoint untuk mengirim permintaan ke backend open-source-backend.vercel.app/kaiwa
    Expects form-data: promt, bab_start, bab_end (semua string), dan optional file 'json'
    """
    # Ambil data dari form
    promt = request.form.get('promt')
    bab_start = request.form.get('bab_start')
    bab_end = request.form.get('bab_end')
    json_file = request.files.get('json')

    # Siapkan data form untuk dikirim ke backend
    data = {
        'promt': promt,
        'bab_start': bab_start,
        'bab_end': bab_end
    }
    files = {}
    # Penjelasan:
    # Ketika file dikirim dari frontend (FormData), Flask akan menerima file tersebut sebagai objek FileStorage.
    # Untuk mengirim file ke backend lain via requests, format tuple-nya: (filename, fileobj, mimetype)
    # Namun, jika fileobj adalah stream (misal .stream), kadang backend tujuan tidak bisa membaca ulang stream yang sudah dibaca.
    # Solusi: gunakan .read() untuk mendapatkan bytes, lalu kirim sebagai io.BytesIO agar bisa dibaca ulang.
    import io
    if json_file:
        file_bytes = json_file.read()
        files['json'] = (json_file.filename, io.BytesIO(file_bytes), json_file.mimetype)
    print(files)
    # Kirim request ke backend
    try:
        backend_url = "https://open-source-backend.vercel.app/kaiwa"
        response = requests.post(backend_url, data=data, files=files)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)