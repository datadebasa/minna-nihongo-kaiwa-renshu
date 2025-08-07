# 📦 Panduan Instalasi MinnaKaiwa

Panduan lengkap untuk menginstal dan menjalankan MinnaKaiwa di lingkungan development dan production.

## 🎯 Prerequisites

### System Requirements

- **OS:** Windows 10+, macOS 10.14+, atau Linux (Ubuntu 18.04+)
- **Python:** 3.8 atau lebih baru
- **Node.js:** 14.0 atau lebih baru (untuk Vercel CLI)
- **Git:** Versi terbaru
- **Memory:** Minimal 2GB RAM
- **Storage:** Minimal 1GB free space

### Software yang Diperlukan

#### Python
```bash
# Windows
# Download dari https://python.org

# macOS
brew install python

# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip
```

#### Node.js
```bash
# Windows
# Download dari https://nodejs.org

# macOS
brew install node

# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### Git
```bash
# Windows
# Download dari https://git-scm.com

# macOS
brew install git

# Ubuntu/Debian
sudo apt install git
```

## 🚀 Instalasi Development

### 1. Clone Repository

```bash
git clone https://github.com/datadebasa/minna-nihongo-kaiwa-renshu.git
cd minna-nihongo-kaiwa-renshu
```

### 2. Setup Virtual Environment

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install development dependencies (opsional)
pip install -r requirements-dev.txt

# Install Vercel CLI
npm install -g vercel
```

### 4. Setup Audio Files

```bash
# Buat direktori audio
mkdir -p api/static/assets/0-0001-01-230001

# Tambahkan file audio dengan format:
# CD_001_001_001.mp3 (Bab 1, Kaiwa)
# CD_001_001_002.mp3 (Bab 1, Renshu)
# dst.
```

### 5. Konfigurasi Environment

```bash
# Buat file .env (opsional)
cp .env.example .env

# Edit file .env sesuai kebutuhan
nano .env
```

### 6. Run Development Server

```bash
# Menggunakan Vercel CLI
vercel dev

# Atau menggunakan Flask langsung
cd api
python index.py
```

Aplikasi akan tersedia di `http://localhost:3000`

## 🐳 Instalasi dengan Docker

### 1. Install Docker

```bash
# Windows/macOS
# Download Docker Desktop dari https://docker.com

# Ubuntu
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER
```

### 2. Build dan Run

```bash
# Build image
docker build -t minnakaiwa .

# Run container
docker run -p 5000:5000 minnakaiwa

# Atau menggunakan Docker Compose
docker-compose up -d
```

## ☁️ Instalasi Production

### Vercel Deployment

```bash
# Login ke Vercel
vercel login

# Deploy
vercel --prod
```

### Manual Deployment

```bash
# Setup server
sudo apt update
sudo apt install nginx python3 python3-pip

# Clone repository
git clone https://github.com/datadebasa/minna-nihongo-kaiwa-renshu.git
cd minna-nihongo-kaiwa-renshu

# Install dependencies
pip3 install -r requirements.txt

# Setup systemd service
sudo nano /etc/systemd/system/minnakaiwa.service
```

Contoh systemd service:
```ini
[Unit]
Description=MinnaKaiwa Flask Application
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/minna-nihongo-kaiwa-renshu
Environment=PATH=/path/to/minna-nihongo-kaiwa-renshu/venv/bin
ExecStart=/path/to/minna-nihongo-kaiwa-renshu/venv/bin/python api/index.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## 🔧 Konfigurasi

### Environment Variables

```bash
# Backend API URL
BACKEND_URL=https://open-source-backend.vercel.app/kaiwa

# Flask environment
FLASK_ENV=production
FLASK_DEBUG=0

# Audio folder path
AUDIO_FOLDER=/path/to/audio/files
```

### Nginx Configuration

```bash
# Copy nginx config
sudo cp nginx.conf /etc/nginx/sites-available/minnakaiwa

# Enable site
sudo ln -s /etc/nginx/sites-available/minnakaiwa /etc/nginx/sites-enabled/

# Test config
sudo nginx -t

# Restart nginx
sudo systemctl restart nginx
```

## 🧪 Testing

### Run Tests

```bash
# Run semua tests
pytest

# Run dengan coverage
pytest --cov=api

# Run specific test
pytest tests/test_app.py::TestHomePage::test_home_page_loads
```

### Code Quality

```bash
# Format code
black api/

# Lint code
flake8 api/

# Security check
bandit -r api/
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Port Already in Use
```bash
# Cek port yang digunakan
lsof -i :5000

# Kill process
kill -9 <PID>
```

#### 2. Audio Files Not Found
```bash
# Cek direktori audio
ls -la api/static/assets/0-0001-01-230001/

# Set permissions
chmod 755 api/static/assets/0-0001-01-230001/
```

#### 3. Vercel CLI Issues
```bash
# Reinstall Vercel CLI
npm uninstall -g vercel
npm install -g vercel

# Clear cache
vercel logout
vercel login
```

#### 4. Python Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Logs

```bash
# Flask logs
tail -f api/logs/app.log

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# System logs
sudo journalctl -u minnakaiwa -f
```

## 📞 Support

Jika mengalami masalah:

1. **Cek dokumentasi** - Lihat [Troubleshooting](troubleshooting.md)
2. **Search issues** - Cari di [GitHub Issues](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu/issues)
3. **Buat issue baru** - Jika masalah belum ada solusi
4. **Hubungi support** - Email ke support@minnakaiwa.com

---

<div align="center">
  <p><strong>MinnaKaiwa - Minna no Nihongo Practice Platform</strong></p>
</div> 