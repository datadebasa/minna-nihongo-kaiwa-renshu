from flask import Flask
from flask import render_template

class Config:
    def gemini_core(self):
        return 'gemini_core'
    
    
gemini = Config()
print(gemini.gemini_core())
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
@app.route('/chat')
def chat():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(debug=True)