# 🧪 Testing Guide - MinnaKaiwa

Panduan lengkap untuk testing aplikasi MinnaKaiwa.

## 📋 Overview

Testing adalah bagian penting dari development cycle MinnaKaiwa. Kami menggunakan berbagai jenis testing untuk memastikan kualitas dan reliability aplikasi.

## 🎯 Testing Strategy

### 1. Unit Testing
- **Scope:** Individual functions dan methods
- **Framework:** pytest
- **Coverage:** Minimal 80%
- **Frequency:** Setiap commit

### 2. Integration Testing
- **Scope:** API endpoints dan database interactions
- **Framework:** pytest dengan Flask test client
- **Coverage:** Semua endpoints
- **Frequency:** Setiap pull request

### 3. End-to-End Testing
- **Scope:** User workflows lengkap
- **Framework:** Manual testing + Browser automation
- **Coverage:** Critical user paths
- **Frequency:** Sebelum release

## 🛠️ Testing Setup

### Prerequisites
```bash
# Install testing dependencies
pip install -r requirements-dev.txt

# Install pytest
pip install pytest pytest-cov pytest-mock
```

### Project Structure
```
tests/
├── __init__.py
├── test_app.py              # Main application tests
├── test_api.py              # API endpoint tests
├── test_audio.py            # Audio functionality tests
├── test_chat.py             # Voice chat tests
└── conftest.py              # Test configuration
```

## 🧪 Running Tests

### Basic Test Execution
```bash
# Run semua tests
pytest

# Run dengan verbose output
pytest -v

# Run dengan coverage
pytest --cov=api

# Run specific test file
pytest tests/test_app.py

# Run specific test function
pytest tests/test_app.py::TestHomePage::test_home_page_loads
```

### Test Categories
```bash
# Run unit tests only
pytest -m unit

# Run integration tests only
pytest -m integration

# Run audio tests
pytest -m audio

# Run chat tests
pytest -m chat

# Run API tests
pytest -m api
```

### Coverage Reports
```bash
# Generate HTML coverage report
pytest --cov=api --cov-report=html

# Generate XML coverage report
pytest --cov=api --cov-report=xml

# Generate terminal coverage report
pytest --cov=api --cov-report=term
```

## 📝 Test Examples

### 1. Homepage Tests
```python
class TestHomePage:
    """Test cases for the home page."""
    
    def test_home_page_loads(self, client):
        """Test that the home page loads successfully."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'MinnaKaiwa' in response.data
    
    def test_home_page_contains_navigation(self, client):
        """Test that the home page contains navigation links."""
        response = client.get('/')
        assert b'Daftar Audio Per Bab' in response.data
        assert b'Mode Chat Suara' in response.data
        assert b'Tentang MinnaKaiwa' in response.data
```

### 2. Audio Tests
```python
class TestAudioPages:
    """Test cases for audio-related pages."""
    
    def test_audio_list_page_loads(self, client):
        """Test that the audio list page loads successfully."""
        response = client.get('/audios')
        assert response.status_code == 200
    
    @patch('os.path.isdir')
    @patch('os.listdir')
    def test_audio_list_with_files(self, mock_listdir, mock_isdir, client):
        """Test audio list page with mock files."""
        mock_isdir.return_value = True
        mock_listdir.return_value = ['CD_001_001_001.mp3', 'CD_001_001_002.mp3']
        
        response = client.get('/audios')
        assert response.status_code == 200
        assert b'CD 001' in response.data
```

### 3. API Tests
```python
class TestAPIEndpoints:
    """Test cases for API endpoints."""
    
    def test_api_message_endpoint(self, client):
        """Test the API message endpoint."""
        response = client.get('/api/v1/message')
        assert response.status_code == 200
        assert b'Hello, Flask!' in response.data
    
    @patch('requests.post')
    def test_kaiwa_proxy_endpoint(self, mock_post, client):
        """Test the kaiwa proxy endpoint."""
        # Mock successful response
        mock_response = MagicMock()
        mock_response.json.return_value = {'status': 'success'}
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        data = {
            'promt': 'test prompt',
            'bab_start': '1',
            'bab_end': '5'
        }
        
        response = client.post('/api/v1/kaiwa', data=data)
        assert response.status_code == 200
        assert b'success' in response.data
```

## 🔧 Test Configuration

### pytest.ini
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
    --color=yes
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
    audio: marks tests related to audio functionality
    chat: marks tests related to chat functionality
    api: marks tests related to API endpoints
```

### conftest.py
```python
import pytest
import os
import sys
from unittest.mock import patch, MagicMock

# Add the api directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'api'))

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    from index import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_audio_files():
    """Mock audio files for testing."""
    return ['CD_001_001_001.mp3', 'CD_001_001_002.mp3']

@pytest.fixture
def mock_chat_response():
    """Mock chat response for testing."""
    return {
        'status': 'success',
        'payload': {
            'output': {
                'response': 'こんにちは！',
                'audio': None
            }
        }
    }
```

## 🎯 Test Categories

### 1. Unit Tests
- **Purpose:** Test individual functions
- **Scope:** Isolated functionality
- **Speed:** Fast execution
- **Dependencies:** Minimal mocking

### 2. Integration Tests
- **Purpose:** Test component interactions
- **Scope:** Multiple components
- **Speed:** Medium execution
- **Dependencies:** Some mocking

### 3. End-to-End Tests
- **Purpose:** Test complete workflows
- **Scope:** Full application
- **Speed:** Slow execution
- **Dependencies:** Real services

## 📊 Test Coverage

### Coverage Goals
- **Overall Coverage:** 80% minimum
- **Critical Paths:** 95% minimum
- **API Endpoints:** 100% coverage
- **Error Handling:** 90% coverage

### Coverage Reports
```bash
# Generate detailed coverage report
pytest --cov=api --cov-report=html --cov-report=term

# Check coverage for specific modules
pytest --cov=api.index --cov-report=term

# Generate coverage badge
pytest --cov=api --cov-report=xml
```

## 🔍 Manual Testing

### 1. Browser Testing
```bash
# Test di browser berbeda
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
```

### 2. Device Testing
```bash
# Test di device berbeda
- Desktop (1024px+)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)
```

### 3. Feature Testing
```bash
# Test fitur utama
- Homepage navigation
- Audio playback
- Voice chat
- Responsive design
```

## 🐛 Debugging Tests

### 1. Verbose Output
```bash
# Run tests dengan verbose output
pytest -v -s

# Run specific test dengan debug
pytest tests/test_app.py::TestHomePage::test_home_page_loads -v -s
```

### 2. Debug Mode
```python
# Tambahkan debug statements
import pdb; pdb.set_trace()

# Atau gunakan ipdb
import ipdb; ipdb.set_trace()
```

### 3. Test Isolation
```bash
# Run test dalam isolation
pytest tests/test_app.py::TestHomePage::test_home_page_loads --tb=short
```

## 📈 Performance Testing

### 1. Load Testing
```bash
# Install locust
pip install locust

# Run load test
locust -f tests/load_test.py
```

### 2. Stress Testing
```python
# Example stress test
def test_concurrent_audio_requests(self, client):
    """Test concurrent audio requests."""
    import threading
    import time
    
    def make_request():
        response = client.get('/audios')
        assert response.status_code == 200
    
    threads = []
    for i in range(10):
        thread = threading.Thread(target=make_request)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
```

## 🔒 Security Testing

### 1. Input Validation
```python
def test_malicious_input(self, client):
    """Test malicious input handling."""
    malicious_inputs = [
        "<script>alert('xss')</script>",
        "../../../etc/passwd",
        "'; DROP TABLE users; --"
    ]
    
    for input_data in malicious_inputs:
        response = client.post('/api/v1/kaiwa', data={'promt': input_data})
        assert response.status_code in [200, 400, 422]
```

### 2. File Upload Security
```python
def test_file_upload_security(self, client):
    """Test file upload security."""
    malicious_files = [
        ('test.exe', b'fake executable'),
        ('test.php', b'<?php echo "hack"; ?>'),
        ('../../../etc/passwd', b'fake content')
    ]
    
    for filename, content in malicious_files:
        response = client.post('/api/v1/kaiwa', data={
            'promt': 'test',
            'json': (filename, content, 'application/octet-stream')
        })
        assert response.status_code in [200, 400, 422]
```

## 📋 Test Checklist

### Pre-commit Checklist
- [ ] All tests pass
- [ ] Coverage > 80%
- [ ] No new warnings
- [ ] Code style compliant
- [ ] Security tests pass

### Pre-release Checklist
- [ ] All test categories pass
- [ ] Manual testing completed
- [ ] Performance tests pass
- [ ] Security tests pass
- [ ] Documentation updated

## 🔗 Related Links

- **Source Code:** [https://github.com/datadebasa/minna-nihongo-kaiwa-renshu](https://github.com/datadebasa/minna-nihongo-kaiwa-renshu)
- **Developer Website:** [https://sodikinnaa.my.id/](https://sodikinnaa.my.id/)
- **Live Demo:** [https://minnakaiwa.vercel.app/](https://minnakaiwa.vercel.app/)

---

<div align="center">
  <p><strong>MinnaKaiwa - Minna no Nihongo Practice Platform</strong></p>
  <p>Testing Guide untuk Platform Pembelajaran Bahasa Jepang 🇯🇵</p>
</div> 