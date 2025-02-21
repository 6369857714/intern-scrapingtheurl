from flask import Flask, send_file
import json
import base64
from io import BytesIO
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask server!"

@app.route('/image')
def image():
    try:
        with open('scraped_data.json') as f:
            data = json.load(f)
        # Decode the base64 image data
        image_data = base64.b64decode(data['image'])  # Ensure the JSON has a key named 'image'
        image = Image.open(BytesIO(image_data))
        image_path = 'image.png'
        image.save(image_path)
        return send_file(image_path, mimetype='image/png')
    except (FileNotFoundError, KeyError):
        return "Image data not found in scraped_data.json", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)























