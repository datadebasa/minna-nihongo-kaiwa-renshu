# 🔌 API Reference - MinnaKaiwa

Dokumentasi lengkap untuk API endpoints MinnaKaiwa.

## 📋 Overview

MinnaKaiwa menggunakan Flask 3 sebagai backend dengan beberapa endpoint utama untuk menangani fitur audio, voice chat, dan pembelajaran bahasa Jepang.

## 🚀 Base URL

```
Development: http://localhost:3000
Production:  https://minna-nihongo-kaiwa-renshu.vercel.app
```

## 📚 Endpoints

### 🏠 Homepage

#### `GET /`
Menampilkan halaman utama aplikasi.

**Response:**
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <title>MinnaKaiwa - Minna no Nihongo Practice</title>
    <!-- ... -->
</head>
<body>
    <!-- Homepage content -->
</body>
</html>
```

### 🎵 Audio Endpoints

#### `GET /audios`
Menampilkan daftar semua file audio yang tersedia.

**Response:**
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <title>MinnaKaiwa - Daftar Audio</title>
    <!-- ... -->
</head>
<body>
    <!-- Audio list content -->
</body>
</html>
```

#### `GET /audios/play/<filename>`
Menampilkan audio player untuk file tertentu.

**Parameters:**
- `filename` (string): Nama file audio (e.g., `CD_001_001_001.mp3`)

**Response:**
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <title>MinnaKaiwa - Audio Player</title>
    <!-- ... -->
</head>
<body>
    <!-- Audio player content -->
</body>
</html>
```

#### `GET /audios/files/<filename>`
Melayani file audio langsung untuk streaming.

**Parameters:**
- `filename` (string): Nama file audio

**Response:**
```
Content-Type: audio/mpeg
Content-Length: <file_size>

<audio_file_binary>
```

### 💬 Chat Endpoints

#### `GET /chat`
Menampilkan interface voice chat.

**Response:**
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <title>MinnaKaiwa - Voice Chat</title>
    <!-- ... -->
</head>
<body>
    <!-- Voice chat interface -->
</body>
</html>
```

### ℹ️ About Endpoints

#### `GET /about`
Menampilkan halaman tentang aplikasi.

**Response:**
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <title>Tentang MinnaKaiwa</title>
    <!-- ... -->
</head>
<body>
    <!-- About page content -->
</body>
</html>
```

### 🔌 API Endpoints

#### `GET /api/v1/message`
Endpoint sederhana untuk testing.

**Response:**
```json
{
  "message": "Hello, Flask!"
}
```

#### `POST /api/v1/kaiwa`
Proxy endpoint untuk mengirim permintaan ke backend AI.

**Request Body:**
```form-data
promt: string          # Input dari user
bab_start: string      # Bab awal (default: "1")
bab_end: string        # Bab akhir (default: "50")
json: file (optional)  # File JSON dengan chat history
```

**Response:**
```json
{
  "status": "success",
  "payload": {
    "output": {
      "response": "string",
      "audio": "string (optional)"
    }
  }
}
```

## 🔧 Error Handling

### 404 Not Found
```html
<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The requested page was not found.</p>
</body>
</html>
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error occurred",
  "status": 500
}
```

## 📊 Response Codes

| Code | Description |
|------|-------------|
| 200 | OK - Request berhasil |
| 404 | Not Found - Resource tidak ditemukan |
| 500 | Internal Server Error - Server error |

## 🔒 Security

### Headers
- `X-Frame-Options: SAMEORIGIN`
- `X-XSS-Protection: 1; mode=block`
- `X-Content-Type-Options: nosniff`

### Rate Limiting
- API endpoints: 10 requests/second
- Login endpoints: 1 request/second

## 📝 Examples

### cURL Examples

#### Get Homepage
```bash
curl -X GET http://localhost:3000/
```

#### Get Audio List
```bash
curl -X GET http://localhost:3000/audios
```

#### Get Audio File
```bash
curl -X GET http://localhost:3000/audios/files/CD_001_001_001.mp3
```

#### Send Chat Message
```bash
curl -X POST http://localhost:3000/api/v1/kaiwa \
  -F "promt=こんにちは" \
  -F "bab_start=1" \
  -F "bab_end=1"
```

### JavaScript Examples

#### Fetch Audio List
```javascript
fetch('/audios')
  .then(response => response.text())
  .then(html => console.log(html));
```

#### Send Chat Message
```javascript
const formData = new FormData();
formData.append('promt', 'こんにちは');
formData.append('bab_start', '1');
formData.append('bab_end', '1');

fetch('/api/v1/kaiwa', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🔗 Related Links

- **Source Code:** [https://github.com/datadebasa/minna-nihongo-kaiwa-renshu](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu)
- **Developer Website:** [https://sodikinnaa.my.id/](https://sodikinnaa.my.id/)
- **Live Demo:** [https://minna-nihongo-kaiwa-renshu.vercel.app/](https://minna-nihongo-kaiwa-renshu.vercel.app/)

---

<div align="center">
  <p><strong>MinnaKaiwa - Minna no Nihongo Practice Platform</strong></p>
  <p>API Documentation untuk Platform Pembelajaran Bahasa Jepang 🇯🇵</p>
</div> 