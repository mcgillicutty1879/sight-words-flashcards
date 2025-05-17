from flask import Flask, jsonify, send_file
from gtts import gTTS
from flask_cors import CORS
import io

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

FLASHCARDS = [
    {"word": "the", "breakdown": ["th", "e"]},
    {"word": "and", "breakdown": ["a", "nd"]},
    {"word": "to", "breakdown": ["t", "o"]},
    {"word": "said", "breakdown": ["s", "ai", "d"]},
    {"word": "you", "breakdown": ["y", "ou"]},
]

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/flashcards')
def flashcards():
    return jsonify(FLASHCARDS)

@app.route('/tts/<text>')
def tts(text):
    tts = gTTS(text=text, lang='en')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return send_file(mp3_fp, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
