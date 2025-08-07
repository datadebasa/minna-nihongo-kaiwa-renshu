# 🤝 Panduan Kontribusi - MinnaKaiwa

Terima kasih telah tertarik untuk berkontribusi pada **MinnaKaiwa**! Platform ini dibuat untuk membantu pembelajar bahasa Jepang di seluruh dunia.

## 📋 Cara Kontribusi

### 🐛 Melaporkan Bug

1. Periksa apakah bug sudah dilaporkan di [Issues](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/issues)
2. Buat issue baru dengan label `bug`
3. Jelaskan bug dengan detail:
   - Langkah reproduksi
   - Perilaku yang diharapkan
   - Screenshot (jika ada)
   - Browser dan OS yang digunakan

### 💡 Mengusulkan Fitur

1. Periksa apakah fitur sudah diusulkan di [Issues](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/issues)
2. Buat issue baru dengan label `enhancement`
3. Jelaskan fitur yang diusulkan:
   - Tujuan dan manfaat
   - Implementasi yang diusulkan
   - Mockup atau wireframe (jika ada)

### 🔧 Kontribusi Kode

#### Setup Development Environment

1. **Fork Repository**
```bash
git clone https://github.com/YOUR_USERNAME/minna-nihongo-kaiwa-renshu.git
cd minna-nihongo-kaiwa-renshu
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
npm install -g vercel
```

3. **Setup Audio Files**
```bash
# Pastikan folder audio tersedia di api/static/assets/0-0001-01-230001/
# Format: CD_001_001_001.mp3, CD_001_001_002.mp3, dst.
```

4. **Run Development Server**
```bash
vercel dev
# atau
cd api && python index.py
```

#### Guidelines

1. **Branch Naming**
   - `feature/nama-fitur` - untuk fitur baru
   - `fix/nama-bug` - untuk perbaikan bug
   - `docs/update-readme` - untuk dokumentasi

2. **Commit Messages**
   - Gunakan bahasa Indonesia atau Inggris
   - Format: `type(scope): description`
   - Contoh: `feat(chat): add voice recognition feature`

3. **Code Style**
   - Python: PEP 8
   - HTML: Indent 4 spaces
   - CSS: Consistent formatting
   - JavaScript: ES6+ standards

4. **Testing**
   - Test fitur baru di browser berbeda
   - Pastikan responsive design tetap baik
   - Test audio functionality

#### Pull Request Process

1. **Buat Branch**
```bash
git checkout -b feature/amazing-feature
```

2. **Commit Changes**
```bash
git add .
git commit -m "feat: add amazing feature"
```

3. **Push ke Fork**
```bash
git push origin feature/amazing-feature
```

4. **Buat Pull Request**
   - Jelaskan perubahan dengan detail
   - Tambahkan screenshot jika ada perubahan UI
   - Link ke issue terkait (jika ada)

## 📁 Struktur Proyek

```
api/
├── index.py              # Flask application
├── templates/            # HTML templates
│   ├── index.html        # Homepage
│   ├── chat.html         # Voice chat
│   ├── about.html        # About page
│   ├── audio_list.html   # Audio listing
│   └── audio_player.html # Audio player
└── static/
    └── assets/           # Audio files
```

## 🎯 Area yang Perlu Kontribusi

### Prioritas Tinggi
- [ ] Menambah bab baru (audio files)
- [ ] Memperbaiki voice recognition
- [ ] Menambah fitur progress tracking
- [ ] Optimasi performa audio

### Prioritas Menengah
- [ ] Menambah dark mode
- [ ] Menambah fitur bookmark
- [ ] Menambah quiz/assessment
- [ ] Menambah offline support

### Prioritas Rendah
- [ ] Menambah animasi UI
- [ ] Menambah sound effects
- [ ] Menambah keyboard shortcuts
- [ ] Menambah accessibility features

## 📝 Code of Conduct

### Perilaku yang Diharapkan
- Bersikap sopan dan menghormati
- Menerima kritik konstruktif
- Fokus pada apa yang terbaik untuk komunitas
- Menunjukkan empati kepada anggota komunitas lain

### Perilaku yang Tidak Diterima
- Penggunaan bahasa atau gambar yang tidak pantas
- Trolling atau komentar yang menghina
- Pelecehan publik atau pribadi
- Menerbitkan informasi pribadi orang lain

## 🏆 Recognition

Kontributor akan diakui di:
- [Contributors](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/graphs/contributors) page
- README.md (untuk kontribusi signifikan)
- Release notes

## 📞 Pertanyaan?

Jika ada pertanyaan tentang kontribusi, silakan:
- Buat issue dengan label `question`
- Hubungi maintainer melalui email
- Diskusikan di Discussions

---

**Terima kasih telah berkontribusi untuk membantu pembelajar bahasa Jepang di seluruh dunia! 🇯🇵**

<div align="center">
  <p><strong>MinnaKaiwa - Minna no Nihongo Practice Platform</strong></p>
</div> 