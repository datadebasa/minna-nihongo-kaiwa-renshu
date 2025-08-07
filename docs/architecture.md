# 🏗️ Arsitektur MinnaKaiwa

Dokumentasi arsitektur sistem MinnaKaiwa - Platform pembelajaran bahasa Jepang.

## 📋 Overview

MinnaKaiwa adalah aplikasi web yang dibangun dengan arsitektur **Monolithic** menggunakan Flask sebagai backend dan HTML/CSS/JavaScript sebagai frontend. Aplikasi ini dirancang untuk deployment di Vercel dengan dukungan serverless functions.

## 🏛️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Layer                            │
├─────────────────────────────────────────────────────────────┤
│  Web Browser (Chrome, Firefox, Safari, Edge)             │
│  • HTML5/CSS3/JavaScript                                  │
│  • Web Speech API                                         │
│  • HTML5 Audio API                                        │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                   Network Layer                            │
├─────────────────────────────────────────────────────────────┤
│  • HTTPS/TLS                                              │
│  • CDN (Vercel Edge Network)                              │
│  • Load Balancing                                         │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                  Application Layer                         │
├─────────────────────────────────────────────────────────────┤
│  Flask 3 Application                                      │
│  ├── Routes & Controllers                                 │
│  ├── Template Rendering                                   │
│  ├── Static File Serving                                  │
│  └── API Endpoints                                        │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                   External Services                        │
├─────────────────────────────────────────────────────────────┤
│  • AI Backend (open-source-backend.vercel.app)           │
│  • Voice Recognition (Web Speech API)                     │
│  • Text-to-Speech (Browser TTS)                          │
└─────────────────────────────────────────────────────────────┘
```

## 🧩 Component Architecture

### 🎨 Frontend Components

#### 1. Homepage (`/`)
```html
├── Navigation Menu
├── Feature Cards
│   ├── Audio Learning
│   ├── Voice Chat
│   └── About
└── Footer
```

#### 2. Audio List (`/audios`)
```html
├── Header
├── Audio File List
│   ├── CD Number
│   ├── Type (Kaiwa/Renshu)
│   └── Play Button
└── Footer
```

#### 3. Audio Player (`/audios/play/<filename>`)
```html
├── Header
├── Audio Controls
│   ├── Play/Pause
│   ├── Progress Bar
│   └── Volume Control
└── Footer
```

#### 4. Voice Chat (`/chat`)
```html
├── Header
│   ├── Language Selector
│   └── Chapter Selector
├── Chat Interface
│   ├── Message Bubbles
│   ├── User Input
│   └── Voice Controls
└── Footer
```

#### 5. About Page (`/about`)
```html
├── Header
├── Content Sections
│   ├── Platform Description
│   ├── Features List
│   ├── Developer Info
│   └── Contact Links
└── Footer
```

### 🔧 Backend Components

#### 1. Flask Application (`api/index.py`)
```python
├── App Configuration
├── Route Definitions
│   ├── GET / (homepage)
│   ├── GET /audios (audio list)
│   ├── GET /audios/play/<filename> (audio player)
│   ├── GET /audios/files/<filename> (file serving)
│   ├── GET /chat (voice chat)
│   ├── GET /about (about page)
│   ├── GET /api/v1/message (test endpoint)
│   └── POST /api/v1/kaiwa (AI proxy)
├── Template Rendering
├── Static File Serving
└── Error Handling
```

#### 2. Template System
```
api/templates/
├── index.html          # Homepage
├── audio_list.html     # Audio listing
├── audio_player.html   # Audio player
├── chat.html          # Voice chat
└── about.html         # About page
```

#### 3. Static Assets
```
api/static/
└── assets/
    └── 0-0001-01-230001/
        ├── CD_001_001_001.mp3
        ├── CD_001_001_002.mp3
        └── ...
```

## 🔄 Data Flow

### 1. User Navigation Flow
```
User Request → Vercel Edge → Flask App → Template Rendering → HTML Response
```

### 2. Audio Streaming Flow
```
Audio Request → Flask App → File System → Audio Stream → Browser Player
```

### 3. Voice Chat Flow
```
Voice Input → Web Speech API → Browser → JavaScript → Flask API → AI Backend → Response → TTS
```

### 4. API Proxy Flow
```
Chat Request → Flask App → AI Backend → Response Processing → JSON Response
```

## 🛠️ Technology Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Styling dan responsive design
- **JavaScript ES6+** - Interaktivitas
- **Web Speech API** - Voice recognition
- **HTML5 Audio API** - Audio playback

### Backend
- **Flask 3** - Web framework
- **Python 3.11+** - Programming language
- **WSGI** - Web server gateway interface

### Deployment
- **Vercel** - Hosting platform
- **Serverless Functions** - Scalable compute
- **Edge Network** - Global CDN

### External Services
- **AI Backend** - Language processing
- **Web Speech API** - Voice recognition
- **Browser TTS** - Text-to-speech

## 🔒 Security Architecture

### 1. Input Validation
```python
# Form data validation
promt = request.form.get('promt')
bab_start = request.form.get('bab_start')
bab_end = request.form.get('bab_end')
```

### 2. File Security
```python
# Secure file serving
if not os.path.isfile(file_path):
    abort(404, description="File tidak ditemukan")
```

### 3. Headers Security
```nginx
# Security headers
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header X-Content-Type-Options "nosniff" always;
```

## 📊 Performance Architecture

### 1. Caching Strategy
- **Static Assets** - 1 year cache
- **Audio Files** - 1 day cache
- **HTML Templates** - No cache (dynamic)

### 2. Compression
```nginx
# Gzip compression
gzip on;
gzip_types text/plain text/css application/json application/javascript;
```

### 3. CDN Integration
- **Vercel Edge Network** - Global distribution
- **Static Assets** - Optimized delivery
- **Audio Files** - Streaming optimization

## 🔍 Monitoring & Logging

### 1. Application Logs
```python
# Flask logging
app.logger.info(f"Memutar audio: {filename}")
app.logger.error(f"File tidak ditemukan: {filename}")
```

### 2. Error Tracking
- **404 Errors** - File not found
- **500 Errors** - Server errors
- **API Errors** - Backend communication

### 3. Performance Monitoring
- **Response Time** - API latency
- **Throughput** - Requests per second
- **Error Rate** - Success/failure ratio

## 🚀 Deployment Architecture

### 1. Development Environment
```
Local Machine → Flask Development Server → http://localhost:3000
```

### 2. Production Environment
```
User Request → Vercel Edge → Serverless Function → Flask App → Response
```

### 3. Docker Environment
```
Docker Container → Nginx → Flask App → Response
```

## 🔧 Configuration Management

### 1. Environment Variables
```bash
FLASK_ENV=production
FLASK_DEBUG=0
BACKEND_URL=https://open-source-backend.vercel.app/kaiwa
```

### 2. Vercel Configuration
```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/api/index" }
  ]
}
```

### 3. Nginx Configuration
```nginx
# Production nginx config
upstream minnakaiwa {
    server minnakaiwa:5000;
}
```

## 🔗 Integration Points

### 1. AI Backend Integration
```python
# API proxy to AI backend
backend_url = "https://open-source-backend.vercel.app/kaiwa"
response = requests.post(backend_url, data=data, files=files)
```

### 2. Web Speech API Integration
```javascript
// Voice recognition
recognition = new window.SpeechRecognition();
recognition.lang = 'ja-JP';
recognition.start();
```

### 3. Audio API Integration
```javascript
// Audio playback
const audio = new Audio(audioUrl);
audio.play();
```

## 📈 Scalability Considerations

### 1. Horizontal Scaling
- **Serverless Functions** - Auto-scaling
- **Edge Network** - Global distribution
- **CDN** - Static asset optimization

### 2. Vertical Scaling
- **Memory Optimization** - Efficient audio handling
- **CPU Optimization** - Async processing
- **Storage Optimization** - Audio file compression

### 3. Performance Optimization
- **Lazy Loading** - Audio files
- **Caching** - Static assets
- **Compression** - Response data

## 🔗 Related Links

- **Source Code:** [https://github.com/datadebasa/minna-nihongo-kaiwa-renshu](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu)
- **Developer Website:** [https://sodikinnaa.my.id/](https://sodikinnaa.my.id/)
- **Live Demo:** [https://minnakaiwa.vercel.app/](https://minnakaiwa.vercel.app/)

---

<div align="center">
  <p><strong>MinnaKaiwa - Minna no Nihongo Practice Platform</strong></p>
  <p>Arsitektur Sistem untuk Platform Pembelajaran Bahasa Jepang 🇯🇵</p>
</div> 