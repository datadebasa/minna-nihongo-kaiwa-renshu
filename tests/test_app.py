"""
Test cases for MinnaKaiwa application
"""

import pytest
import os
import sys
from unittest.mock import patch, MagicMock

# Add the api directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'api'))

from index import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

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
    
    @patch('os.path.isdir')
    def test_audio_list_no_directory(self, mock_isdir, client):
        """Test audio list page when directory doesn't exist."""
        mock_isdir.return_value = False
        
        response = client.get('/audios')
        assert response.status_code == 200

class TestChatPage:
    """Test cases for the chat page."""
    
    def test_chat_page_loads(self, client):
        """Test that the chat page loads successfully."""
        response = client.get('/chat')
        assert response.status_code == 200
        assert b'MinnaKaiwa - Voice Chat' in response.data

class TestAboutPage:
    """Test cases for the about page."""
    
    def test_about_page_loads(self, client):
        """Test that the about page loads successfully."""
        response = client.get('/about')
        assert response.status_code == 200
        assert b'Tentang MinnaKaiwa' in response.data
        assert b'Minna no Nihongo' in response.data

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

class TestErrorHandling:
    """Test cases for error handling."""
    
    def test_404_error(self, client):
        """Test 404 error handling."""
        response = client.get('/nonexistent-page')
        assert response.status_code == 404

class TestAudioFileServing:
    """Test cases for audio file serving."""
    
    @patch('os.path.isfile')
    def test_serve_audio_file_exists(self, mock_isfile, client):
        """Test serving audio file when it exists."""
        mock_isfile.return_value = True
        
        with patch('flask.send_from_directory') as mock_send:
            mock_send.return_value = 'audio content'
            response = client.get('/audios/files/test.mp3')
            assert response.status_code == 200
    
    @patch('os.path.isfile')
    def test_serve_audio_file_not_exists(self, mock_isfile, client):
        """Test serving audio file when it doesn't exist."""
        mock_isfile.return_value = False
        
        response = client.get('/audios/files/nonexistent.mp3')
        assert response.status_code == 200  # Should render template, not 404

class TestConfiguration:
    """Test cases for application configuration."""
    
    def test_config_class(self):
        """Test the Config class."""
        from index import Config
        config = Config()
        assert config.gemini_core() == 'gemini_core'

if __name__ == '__main__':
    pytest.main([__file__]) 