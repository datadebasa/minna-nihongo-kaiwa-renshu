# 📚 MinnaKaiwa - Minna no Nihongo Practice Platform

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fdatadebasa%2Fminna-nihongo-kaiwa-renshu&demo-title=MinnaKaiwa&demo-description=Japanese%20Learning%20Platform%20based%20on%20Minna%20no%20Nihongo&demo-url=https%3A%2F%2Fminnakaiwa.vercel.app%2F&demo-image=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1669994156%2Frandom%2Fflask.png)

## 🎯 Tentang MinnaKaiwa

MinnaKaiwa adalah platform latihan bahasa Jepang yang berbasis pada kurikulum **Minna no Nihongo**. Platform ini dirancang untuk membantu pembelajar bahasa Jepang berlatih percakapan dan latihan secara interaktif.

### ✨ Fitur Utama

- **🗣️ Kaiwa (Percakapan)** - Latihan percakapan bahasa Jepang per bab
- **📖 Renshu (Latihan)** - Latihan tata bahasa dan kosakata per bab
- **🎵 Audio Learning** - Pemutaran audio pembelajaran per bab
- **💬 Voice Chat** - Mode chat suara untuk latihan berbicara
- **📱 Responsive Design** - Berfungsi optimal di desktop dan mobile

### 🎓 Berdasarkan Minna no Nihongo

Platform ini menggunakan kurikulum standar **Minna no Nihongo** yang merupakan buku pembelajaran bahasa Jepang yang paling populer dan diakui secara internasional. Setiap bab disesuaikan dengan struktur pembelajaran buku tersebut.

## 🚀 Demo

**Live Demo:** [https://minna-nihongo-kaiwa-renshu.vercel.app/](https://minna-nihongo-kaiwa-renshu.vercel.app/)

## 🛠️ Teknologi

- **Backend:** Flask 3 (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Deployment:** Vercel
- **Audio Processing:** Native HTML5 Audio API
- **Voice Chat:** Web Speech API

## 📦 Instalasi & Penggunaan

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Langkah Instalasi

1. **Clone Repository**
```bash
git clone https://github.com/datadebasa/minna-nihongo-kaiwa-renshu.git
cd minna-nihongo-kaiwa-renshu
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Setup Audio Files**
```bash
# Pastikan folder audio tersedia di api/static/assets/0-0001-01-230001/
# Format file: CD_001_001_001.mp3, CD_001_001_002.mp3, dst.
```

4. **Run Locally**
```bash
# Menggunakan Vercel CLI
npm i -g vercel
vercel dev

# Atau menggunakan Flask langsung
cd api
python index.py
```

Aplikasi akan tersedia di `http://localhost:3000`

## 📁 Struktur Proyek

```
minna-nihongo-kaiwa-renshu/
├── api/
│   ├── index.py              # Flask application
│   ├── templates/            # HTML templates
│   │   ├── index.html        # Homepage
│   │   ├── chat.html         # Voice chat interface
│   │   ├── about.html        # About page
│   │   ├── audio_list.html   # Audio listing
│   │   └── audio_player.html # Audio player
│   └── static/
│       └── assets/           # Audio files
├── requirements.txt           # Python dependencies
├── vercel.json              # Vercel configuration
└── README.md               # This file
```

## 🎵 Format Audio

Audio files harus mengikuti format:
- **Kaiwa:** `CD_001_001_001.mp3` (Bab 1, Kaiwa)
- **Renshu:** `CD_001_001_002.mp3` (Bab 1, Renshu)

## 🔧 Konfigurasi

### Environment Variables

```bash
# Backend API URL (opsional)
BACKEND_URL=https://open-source-backend.vercel.app/kaiwa
```

### Vercel Configuration

File `vercel.json` sudah dikonfigurasi untuk deployment otomatis di Vercel.

## 🚀 Deployment

### One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fdatadebasa%2Fminna-nihongo-kaiwa-renshu)

### Manual Deployment

1. Push ke GitHub repository
2. Connect dengan Vercel
3. Deploy otomatis

## 🤝 Kontribusi

Kontribusi sangat welcome! Silakan:

1. Fork repository ini
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Kontak

- **GitHub:** [@datadebasa](https://github.com/datadebasa)
- **Developer Website:** [https://sodikinnaa.my.id/](https://sodikinnaa.my.id/)
- **Project Link:** [https://github.com/datadebasa/minna-nihongo-kaiwa-renshu](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu)

## 🙏 Acknowledgments

- **Minna no Nihongo** - Kurikulum pembelajaran bahasa Jepang
- **Flask** - Web framework untuk Python
- **Vercel** - Platform deployment
- **Web Speech API** - Voice recognition technology
- **Sodikin** - Developer utama platform ini

---

<div align="center">
  <p>Made with ❤️ for Japanese learners worldwide</p>
  <p><strong>MinnaKaiwa - Minna no Nihongo Practice Platform</strong></p>
</div>
