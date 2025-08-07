# 🤝 Contributing Guide - MinnaKaiwa

Panduan lengkap untuk berkontribusi pada proyek MinnaKaiwa.

## 📋 Overview

Kami sangat menghargai kontribusi dari komunitas! MinnaKaiwa adalah proyek open source yang bertujuan membantu pembelajar bahasa Jepang di seluruh dunia.

## 🎯 Cara Kontribusi

### 🐛 Melaporkan Bug

1. **Cek Issues Terlebih Dahulu**
   - Periksa [GitHub Issues](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/issues)
   - Pastikan bug belum dilaporkan

2. **Buat Issue Baru**
   - Gunakan template issue yang tersedia
   - Jelaskan bug dengan detail
   - Sertakan screenshot jika relevan

3. **Informasi yang Diperlukan**
   - Langkah reproduksi yang jelas
   - Perilaku yang diharapkan
   - Environment (OS, Browser, dll)
   - Error messages atau logs

### 💡 Mengusulkan Fitur

1. **Cek Fitur Terlebih Dahulu**
   - Periksa roadmap proyek
   - Pastikan fitur belum diusulkan

2. **Buat Feature Request**
   - Jelaskan manfaat fitur
   - Berikan use case yang jelas
   - Sertakan mockup jika ada

3. **Diskusikan dengan Komunitas**
   - Libatkan maintainer dan kontributor lain
   - Pertimbangkan feedback dari komunitas

### 🔧 Kontribusi Kode

#### Setup Development Environment

1. **Fork Repository**
```bash
git clone https://github.com/YOUR_USERNAME/minna-nihongo-kaiwa-renshu.git
cd minna-nihongo-kaiwa-renshu
```

2. **Setup Environment**
```bash
# Buat virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

3. **Setup Audio Files**
```bash
# Buat direktori audio
mkdir -p api/static/assets/0-0001-01-230001

# Tambahkan file audio test
# CD_001_001_001.mp3, CD_001_001_002.mp3, dst.
```

4. **Run Development Server**
```bash
# Menggunakan Vercel CLI
npm install -g vercel
vercel dev

# Atau menggunakan Flask langsung
cd api
python index.py
```

#### Development Guidelines

1. **Code Style**
   - Python: PEP 8
   - HTML: 4 spaces indent
   - CSS: Consistent formatting
   - JavaScript: ES6+ standards

2. **Commit Messages**
   - Format: `type(scope): description`
   - Contoh: `feat(chat): add voice recognition feature`
   - Types: feat, fix, docs, style, refactor, test, chore

3. **Testing**
   - Tulis test untuk fitur baru
   - Pastikan semua test pass
   - Maintain coverage > 80%

4. **Documentation**
   - Update README jika perlu
   - Tambahkan docstrings untuk fungsi baru
   - Update API documentation

#### Pull Request Process

1. **Buat Branch**
```bash
git checkout -b feature/amazing-feature
# atau
git checkout -b fix/bug-description
```

2. **Develop Feature**
   - Tulis kode dengan clean
   - Test secara lokal
   - Commit dengan message yang jelas

3. **Push ke Fork**
```bash
git add .
git commit -m "feat: add amazing feature"
git push origin feature/amazing-feature
```

4. **Buat Pull Request**
   - Gunakan template PR yang tersedia
   - Jelaskan perubahan dengan detail
   - Link ke issue terkait
   - Sertakan screenshot jika ada perubahan UI

## 📁 Struktur Proyek

```
minna-nihongo-kaiwa-renshu/
├── api/
│   ├── index.py              # Flask application
│   ├── templates/            # HTML templates
│   │   ├── index.html        # Homepage
│   │   ├── chat.html         # Voice chat
│   │   ├── about.html        # About page
│   │   ├── audio_list.html   # Audio listing
│   │   └── audio_player.html # Audio player
│   └── static/
│       └── assets/           # Audio files
├── tests/                    # Test files
├── docs/                     # Documentation
├── requirements.txt           # Python dependencies
├── requirements-dev.txt       # Development dependencies
├── vercel.json              # Vercel configuration
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose
├── nginx.conf               # Nginx configuration
├── Makefile                 # Development commands
├── pytest.ini              # Test configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
├── README.md               # Project documentation
├── CONTRIBUTING.md         # This file
├── CHANGELOG.md           # Version history
├── LICENSE                 # MIT License
└── SECURITY.md            # Security policy
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

## 🛠️ Development Tools

### Code Quality
```bash
# Format code
black api/
isort api/

# Lint code
flake8 api/
pylint api/

# Type checking
mypy api/
```

### Testing
```bash
# Run tests
pytest

# Run dengan coverage
pytest --cov=api

# Run specific test
pytest tests/test_app.py::TestHomePage::test_home_page_loads
```

### Security
```bash
# Security check
bandit -r api/
safety check
```

### Pre-commit Hooks
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run hooks
pre-commit run --all-files
```

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

### Kontributor Recognition
- **GitHub Contributors** - Otomatis di GitHub
- **README.md** - Untuk kontribusi signifikan
- **Release Notes** - Untuk setiap release
- **Hall of Fame** - Untuk kontributor aktif

### Contribution Levels
- **Bronze** - 1-5 contributions
- **Silver** - 6-15 contributions
- **Gold** - 16+ contributions
- **Platinum** - Maintainer level

## 📞 Getting Help

### Resources
- **Documentation** - Lihat [docs/](docs/) folder
- **Issues** - [GitHub Issues](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/issues)
- **Discussions** - [GitHub Discussions](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/discussions)

### Contact
- **Email** - support@minnakaiwa.com
- **Developer Website** - [https://sodikinnaa.my.id/](https://sodikinnaa.my.id/)

## 🔗 Quick Links

- **Source Code:** [https://github.com/datadebasa/minna-nihongo-kaiwa-renshu](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu)
- **Live Demo:** [https://minnakaiwa.vercel.app/](https://minnakaiwa.vercel.app/)
- **Issues:** [https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/issues](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/issues)
- **Pull Requests:** [https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/pulls](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/pulls)

## 📋 Checklist

### Pre-commit Checklist
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Coverage > 80%
- [ ] No new warnings
- [ ] Documentation updated
- [ ] Security check passed

### Pull Request Checklist
- [ ] Feature/fix is complete
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Code review completed
- [ ] All CI checks pass
- [ ] Ready for merge

---

**Terima kasih telah berkontribusi untuk membantu pembelajar bahasa Jepang di seluruh dunia! 🇯🇵**

<div align="center">
  <p><strong>MinnaKaiwa - Minna no Nihongo Practice Platform</strong></p>
  <p>Membangun komunitas pembelajaran bahasa Jepang yang inklusif dan mendukung</p>
</div> 